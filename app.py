import telebot
from settings import bot, WEBHOOK_SECRET, WEBHOOK_URL
from flask import Flask, request, abort



# for polling for messages
# bot.infinity_polling() 

app = Flask(__name__)

@app.route(f"/webhook", methods=["POST"])
def webhook():
    if request.headers.get("content-type") == "application/json":
        json_string = request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    
    else:
        abort(403)


import bot_message_handlers

if __name__ == "__main__":
    # remove previous hook and set new hook
    bot.set_webhook(url=WEBHOOK_URL, secret_token=WEBHOOK_SECRET)
    print("BOT ONLINE!!!!!")
    app.run(host="0.0.0.0", port=5000)