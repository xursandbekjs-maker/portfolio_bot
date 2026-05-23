import telebot
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu aleykum, men Xursandbek Jumaboyev. \nBu mening portfolio botim. \nQuyidagi bo'limlardan birini tanlang:")
	
bot.infinity_polling()