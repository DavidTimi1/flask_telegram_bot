from settings import bot, WEBHOOK_SECRET, WEBHOOK_URL
import bot_message_handlers

print("BOT ONLINE!!!!!")

bot.remove_webhook()

# for polling for messages
# bot.infinity_polling() 

# using webhook
bot.set_webhook(WEBHOOK_URL, secret_token=WEBHOOK_SECRET)