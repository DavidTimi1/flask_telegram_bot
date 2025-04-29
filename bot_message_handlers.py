import os

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from json import loads as json_loads, dumps as json_dumps

from settings import bot, HELP_WEBSITE, TG_MINI_APP_URL
from gemini import ask_gemini


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Open Mini App", TG_MINI_APP_URL))
    markup.add(InlineKeyboardButton("Open Website", HELP_WEBSITE))
    markup.add(InlineKeyboardButton("Share Bot", switch_inline_query="Check out this bot!"))


    bot.reply_to(
        message, 
        "Howdy, how are you doing? I will now be giving Gemini responses", 
        reply_markup=markup
    )


@bot.message_handler(commands=['help'])
def help(message):
    person = message.from_user
    first_name = person.first_name
    chat_id = message.chat.id

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Open Website", HELP_WEBSITE))
    
    reply = f"Hi!! {first_name}, how may I help?"
    bot.send_message(chat_id, reply, reply_markup=markup)


@bot.message_handler(commands=['clear'])
def clear(message):
    person = message.from_user
    username = person.username

    delete_file(username)
    # delete messages too


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    person = message.from_user
    username = person.username
    history = retrieve_chat_history(username)

    response = ask_gemini(message.text, history=history)

    save_chat_state(username, history)

    bot.reply_to(message, response)


@bot.message_handler(content_types=['document', 'photo', 'audio', 'video', 'voice'])
def handle_file_upload(message):
    person = message.from_user
    username = person.username
    chat_id = message.chat.id


    # Handle different file types
    if message.document:
        file_obj = message.document
        file_name = f"{username}_document.bin"
    elif message.photo:
        file_obj = message.photo[-1]
        print(message.photo)
        file_name = f"{username}_photo.jpg"
        file_obj.mime_type = "image/jpeg"
    elif message.audio:
        file_obj = message.audio
        file_name = f"{username}_audio.mp3"
    elif message.video:
        file_obj = message.video
        file_name = f"{username}_video.mp4"
    elif message.voice:
        file_obj = message.voice
        file_name = f"{username}_voice.ogg"
    else:
        bot.send_message(chat_id, "Unsupported file type.")
        return

    # Download the file
    
    file_info = bot.get_file(file_obj.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_path = f"files/{file_info.file_path or file_name}"
    print ("file", file_obj)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # Save the file
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Use caption or default prompt
    caption = message.caption if message.caption else "Tell me about the file"
    history = retrieve_chat_history(username)

    # Query Gemini with the file path and caption
    response = ask_gemini(caption, history=history, file_path=file_path, mime_type=file_obj.mime_type)

    save_chat_state(username, history)

    bot.send_message(chat_id, response)



def retrieve_chat_history(name):
    history = []

    if not os.path.isfile(f"chats/{name}.json"):
        file = open(f"chats/{name}.json", 'x')
        file.close()
        
    else:
        with open(f"chats/{name}.json") as f:
            data = f.read()
            history = json_loads(data) if data else []

    return history


def save_chat_state(name, history):
    data = json_dumps(history, indent=4)
    with open(f"chats/{name}.json", 'w') as file:
        file.write(data)


def delete_file(name):
    os.remove(f"chats/{name}.json")

def abs_path(x):
    return os.path.abspath(x)



# def start(bot, update):
#     bot.send_message(chat_id = update.message.chat_id, text = reply) #sending message

# def help(bot,update):
#     reply = "How can I help You?"
#     bot.send_message(chat_id = update.message.chat_id, text = reply)  #sending message

# def echo_text(bot,update):
#     reply = update.message.text
#     bot.send_message(chat_id = update.message.chat_id, text = reply)

# def sticker(bot,update):
#     reply = update.message.sticker.file_id
#     bot.send_sticker(chat_id = update.message.chat_id, sticker = reply)

# def error(bot,update):
#     print(f"Shit!! Update {update} caused error {update.error}")


# def main():
#     updater = Updater(TOKEN)  #take the updates
#     dp = updater.dispatcher   #handle the updates

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("help", help))
#     dp.add_handler(MessageHandler(Filters.text, echo_text))   #if the user sends text
#     dp.add_handler(MessageHandler(Filters.sticker, sticker))  #if the user sends sticker
#     dp.add_error_handler(error)
#     updater.start_polling()
#     print("Started...")
#     updater.idle()
