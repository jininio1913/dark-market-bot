import telebot
import os

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

users = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    
    if user_id not in users:
        users[user_id] = 100
    
    bot.reply_to(message, f"🔥 مرحبا بك في لعبة الكنز!\n💰 رصيدك: {users[user_id]}$")

@bot.message_handler(commands=['balance'])
def balance(message):
    user_id = message.from_user.id
    
    if user_id in users:
        bot.reply_to(message, f"💰 رصيدك الحالي: {users[user_id]}$")
    else:
        bot.reply_to(message, "استعمل /start أولاً")

bot.infinity_polling()
