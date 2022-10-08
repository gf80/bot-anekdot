# -*- coding: utf-8 -*-
from config import TOKEN
import telebot
from telebot import types

bot = telebot.TeleBot(token=TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Да', callback_data='joke')
    item2 = types.InlineKeyboardButton('Конечно', callback_data='joke')
    markup.add(item1,item2)
    bot.send_message(message.chat.id, "Хочешь расскажу тебе шутку?", reply_markup=markup)


@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    try:
        if call.message:
            if call.data == 'joke':
                bot.send_message(call.message.chat.id, "hahahhahaha")
    except:
        ...
bot.infinity_polling(timeout=10, long_polling_timeout=5)