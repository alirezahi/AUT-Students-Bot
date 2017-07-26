import telebot
from config import *
from pymongo import MongoClient
import urllib
from urllib import request
import json

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

@telebot.message_handler(content_types=['photo'])
def some_function_second(message):
    file_id = message.photo[-1]
    print(file_id)
    result = urllib.request.urlopen('https://api.telegram.org/bot'+api_key+'/getFile?file_id='+file_id.file_id).read().decode('utf-8')
    result = json.loads(result)
    print(result['result']['file_path'])
    urllib.request.urlretrieve('https://api.telegram.org/file/bot'+api_key+'/'+result['result']['file_path'],result['result']['file_path'].split('/')[1])
    telebot.reply_to(message, 'yeap yeap photo', reply_markup=markup)

telebot.polling()