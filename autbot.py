import telebot
from config import *
from pymongo import MongoClient

telebot = telebot.TeleBot(api_key)

from telebot import types

markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)

@telebot.message_handler(func=lambda m: True)
def some_function(message):
    client = MongoClient()
    db = client.aut
    print(message.text)
    result = db.students.find({'std_id': int(message.text.strip())})
    print(result)
    for res in result:
        print(res)
        telebot.reply_to(message, res['name'], reply_markup=markup)

telebot.polling()