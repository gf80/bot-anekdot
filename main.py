# -*- coding: utf-8 -*-
import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(token=TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Да")
    item2 = item1 = types.KeyboardButton("Конечно :)")
    markup.add(item1,item2)
    bot.send_message(message.chat.id, "Хочешь расскажу тебе шутку?", reply_markup=markup)