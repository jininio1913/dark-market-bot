import telebot
import random
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

players = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    
    if user_id not in players:
        players[user_id] = {"gold": 500}
    
    gold = players[user_id]["gold"]
    
    bot.send_message(message.chat.id,
        f"🏴‍☠️ مرحباً بك في السوق المظلم\n\n"
        f"💰 ذهبك الحالي: {gold}\n\n"
        f"اكتب /map لشراء خريطة كنز مقابل 300 ذهب."
    )

@bot.message_handler(commands=['map'])
def treasure_map(message):
    user_id = message.from_user.id
    
    if user_id not in players:
        bot.send_message(message.chat.id, "اكتب /start أولاً.")
        return
    
    gold = players[user_id]["gold"]
    
    if gold < 300:
        bot.send_message(message.chat.id, "❌ لا تملك ذهب كافي.")
        return
    
    players[user_id]["gold"] -= 300
    result = random.randint(1, 100)
    
    if result <= 40:
        reward = 200
        text = "وجدت كنز صغير!"
    elif result <= 90:
        reward = 450
        text = "وجدت كنز متوسط!"
    elif result <= 99:
        reward = 1200
        text = "🔥 وجدت كنز أسطوري!"
    else:
        players[user_id]["gold"] = 0
        bot.send_message(message.chat.id, "💀 الخريطة مزورة! خسرت كل ذهبك.")
        return
    
    players[user_id]["gold"] += reward
    
    bot.send_message(message.chat.id,
        f"{text}\n\n💰 ذهبك الحالي: {players[user_id]['gold']}"
    )

bot.polling()
