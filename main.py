import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Men haqimda")
    btn2 = types.KeyboardButton("Loyihalarim")
    btn3 = types.KeyboardButton("Bog'lanish")
    btn4 = types.KeyboardButton("Bilimlarim")	
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    text = "Assalomu aleykum, men Xursandbek Jumaboyev. \nBu mening portfolio botim. \nQuyidagi bo'limlardan birini tanlang"
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(func=lambda m: m.text == "Men haqimda")
def aboutme_handler(message):
    text = "Men Xursandbek Jumaboyev frontend dasturchiman.\nHozirda ReactJS va NextJS bilan ishlayman.\nShuningdek, backend uchun NodeJS va ExpressJS dan foydalanaman.\nMening maqsadim, foydalanuvchilarga qulay va samarali veb-ilovalar yaratishdir."

    bot.send_message(message.chat.id, text, reply_markup="keyboard")

@bot.message_handler(func=lambda m: m.text == "Loyihalarim")
def projects_handler(message):
    text = "Mening loyihalarim:\n1. Portfolio veb-sayti - ReactJS va NextJS yordamida yaratilgan shaxsiy portfolio saytim.\n2. Blog platformasi - NodeJS va ExpressJS yordamida yaratilgan blog platformasi, foydalanuvchilar o'z maqolalarini yaratishlari va boshqalar bilan bo'lishishlari mumkin.\n3. To-do ro'yxati ilovasi - ReactJS yordamida yaratilgan to-do ro'yxati ilovasi, foydalanuvchilar o'z vazifalarini qo'shishlari, tahrirlashlari va o'chirishlari mumkin."

    bot.send_message(message.chat.id, text, reply_markup="keyboard")

@bot.message_handler(func=lambda m: m.text == "Bog'lanish")
def contact_handler(message):
    text = "Men bilan bog'lanish uchun quyidagi manzillar orqali yozishingiz mumkin:\nEmail: xursandbek.jumaboyev@example.com\nTelegram: @xursandbek_jumaboyev"

    bot.send_message(message.chat.id, text, reply_markup="keyboard")

@bot.message_handler(func=lambda m: m.text == "Bilimlarim")
def skills_handler(message):
    text = "Mening bilimlarim:\n- Frontend: ReactJS, NextJS, HTML, CSS, JavaScript\n- Backend: NodeJS, ExpressJS\n- Boshqa: Git, MongoDB"

    bot.send_message(message.chat.id, text, reply_markup="keyboard")
bot.infinity_polling()