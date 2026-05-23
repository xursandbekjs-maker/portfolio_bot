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

	
bot.infinity_polling()