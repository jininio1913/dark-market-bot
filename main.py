import telebot

TOKEN = "HTTP API:
8631434820:AAH-AH_dPDZGwhucsQAjLQihO9yR52Dw_8s"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبا بك في لعبة الكنز 👑🔥")

bot.infinity_polling()
