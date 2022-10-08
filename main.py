# -*- coding: utf-8 -*-
import sqlite3
from config import TOKEN
import telebot
from telebot import types
import random2 as random

bot = telebot.TeleBot(token=TOKEN)

con = sqlite3.connect('a.db',check_same_thread=False)
cursor = con.cursor()

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Да', callback_data='joke')
    item2 = types.InlineKeyboardButton('Конечно', callback_data='joke')
    markup.add(item1,item2)
    bot.send_message(message.chat.id, "Хочешь расскажу тебе шутку?", reply_markup=markup)

def joke(message):
    cursor.execute(f'SELECT * FROM a WHERE id = {random.randint(1,32640)}')
    record = cursor.fetchall()
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Смешно')
    item2 = types.KeyboardButton('Давай еще одну')
    markup.add(item1,item2)
    bot.send_message(message.chat.id, text=[i[1] for i in record], reply_markup=markup)


@bot.message_handler(content_types='text')
def answer(message):
    if message.chat.type == 'private':
        if message.text == 'Смешно' or message.text == 'Давай еще одну':
            joke(message)
        else:
            bot.send_message(message.chat.id, "Что думаешь, самый умный. Я тебя все равно не понимаю)))")

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'joke':
            joke(call.message)


bot.infinity_polling(timeout=10, long_polling_timeout=5)