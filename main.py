import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# Keyboard ni bir marta funksiya sifatida yozing
def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Men haqimda"), types.KeyboardButton("Loyihalarim"))
    keyboard.add(types.KeyboardButton("Bog'lanish"), types.KeyboardButton("Bilimlarim"))
    return keyboard

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = "Assalomu aleykum, men Xursandbek Jumaboyev.\nBu mening portfolio botim.\nQuyidagi bo'limlardan birini tanlang"
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())  # ✅

@bot.message_handler(func=lambda m: m.text == "Men haqimda")
def aboutme_handler(message):
    text = "Men Xursandbek Jumaboyev frontend dasturchiman.\n"
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())  # ✅

@bot.message_handler(func=lambda m: m.text == "Loyihalarim")
def projects_handler(message):
    text = "Mening loyihalarim:\n..."
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())  # ✅

@bot.message_handler(func=lambda m: m.text == "Bog'lanish")
def contact_handler(message):
    text = "Men bilan bog'lanish...\n..."
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())  # ✅

@bot.message_handler(func=lambda m: m.text == "Bilimlarim")
def skills_handler(message):
    text = "Mening bilimlarim:\n..."
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())  # ✅

bot.infinity_polling()