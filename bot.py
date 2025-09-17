import telebot

# Вставь сюда свой токен
TOKEN = "8207771435:AAG4NPvgm-b3mDFR8adLrJb0JI4RREQB_Zs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я твой бот ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
