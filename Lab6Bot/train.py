from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import requests
from aiogram.utils import executor

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

TOKEN = '5086695702:AAFduCBMMovZdojz-NLaKt5Jlyirm3P-QhU'

mes_cat = 'Cat fact'
mes_dog = 'Dog fact'
mes_trans = 'Translate'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def answer_all(message):
    text = message.text
    print('--------')
    print(text)
    if text == mes_cat:
        await message.answer(get_cat_fact(), reply=False)
    elif text == mes_dog:
        await message.answer(get_dog_fact(), reply=False)
    else:
        print('ENTERED')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [mes_cat, mes_dog, mes_trans]
        keyboard.add(*buttons)
        await message.answer('Smash the button', reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp)