import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Men haqimda")
    btn2 = types.KeyboardButton("Loyihalarim")	
    keyboard.add(btn1, btn2)
    text = "Assalomu aleykum, men Xursandbek Jumaboyev. \nBu mening portfolio botim. \nQuyidagi bo'limlardan birini tanlang"
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(func=lambda m: True)
def replybutton_handler(message):
    if message.text == "Men haqimda":
        bot.send_message(message.chat.id, "Bu qism qo'shiladi")
    bot.reply_to(message, message.text)
	
bot.infinity_polling()