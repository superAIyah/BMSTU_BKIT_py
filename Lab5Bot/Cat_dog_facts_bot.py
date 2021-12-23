import requests
import telebot
from telebot import types

def get_cat_fact():
    url = 'http://cat-fact.herokuapp.com/facts/random'
    res = requests.get(url)
    json = res.json()
    return str(json['text'])

def get_dog_fact():
    url = 'http://dog-api.kinduff.com/api/facts'
    res = requests.get(url)
    json = res.json()
    return str(*json['facts'])

# Токен бота
TOKEN = '5086695702:AAFduCBMMovZdojz-NLaKt5Jlyirm3P-QhU'

# Сообщения
mes_cat = 'Cat fact'
mes_dog = 'Dog fact'

# Создание бота
bot = telebot.TeleBot(TOKEN)

# Обработчик событий
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Идентификатор диалога
    chat_id = message.chat.id

    # Текст, введенный пользователем, то есть текст с кнопки
    text = message.text

    # Проверка сообщения и вывод данных
    if text == mes_cat:
        #bot.send_message(chat_id, "Кошка")
        bot.send_message(chat_id, get_cat_fact())
    elif text == mes_dog:
        #bot.send_message(chat_id, "Собака")
        bot.send_message(chat_id, get_dog_fact())
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton(mes_cat)
        itembtn2 = types.KeyboardButton(mes_dog)
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id, 'Smash the button', reply_markup=markup)
bot.infinity_polling()