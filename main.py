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
    text = "Men Xursandbek Jumaboyev frontend dasturchiman.\n Men 2025-yildan beri dasturlash bilan shug'ullanaman va ko'plab loyihalarda ishtirok etganman."
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())  # ✅

@bot.message_handler(func=lambda m: m.text == "Loyihalarim")
def projects_handler(message):
    text = """ 
Loyihalarim

Tibbiy yordam xizmati vebsayti: [Website](https://medical-assistance2.vercel.app)
Matnni lotindan kirillga, kirilldan lotinga o'tkazuvchi Telegram bot: [Bot](https://t.me/kirill_to_latin_converters_bot)"""
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_keyboard())  # ✅

@bot.message_handler(func=lambda m: m.text == "Bog'lanish")
def contact_handler(message):
    text = "Men bilan bog'lanish .\n Email:xursandbekjumaboyev987@gmail.com\n Telegram: @jumaboyev_x27\n LinkedIn: https://www.linkedin.com/in/xursandbek-jumaboyev-123456789/"
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_keyboard())  # ✅

@bot.message_handler(func=lambda m: m.text == "Bilimlarim")
def skills_handler(message):
    text = "Mening bilimlarim:\n - HTML, CSS, JavaScript\n- React.js\n- Node.js\n- Git va GitHub\n- Responsive dizayn"
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_keyboard())  # ✅

bot.infinity_polling()