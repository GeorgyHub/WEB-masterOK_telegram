#libraries
import telebot
from telebot import types

bot = telebot.TeleBot('5724910036:AAFyHAgSa0qKelg_UTCnwaLpZ1oDT8iO0jM')

#functions
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Старт")
    markup.add(button1)

    hello = f'Добро пожаловать в <b>WEB-мастерОК</b>. Чем могу вам помочь?'

    bot.send_message(message.chat.id, hello, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Привет,", parse_mode='html')

@bot.message_handler()
def get_text(message):
    bot.send_message(message.chat.id, 'Используй команды')

bot.polling(none_stop=True)