import unittest

import requests
from googletrans import Translator

def get_cat_fact():
    url = 'http://cat-fact.herokuapp.com/facts/random'
    res = requests.get(url)
    return res.status_code

def get_dog_fact():
    url = 'http://dog-api.kinduff.com/api/facts'
    res = requests.get(url)
    return res.status_code

def translate_fact(text):
    translator = Translator()
    translation = translator.translate(text, dest='ru')
    return translation.text

class MyTestCase(unittest.TestCase):

    def test_status_code_cat(self): # тест кода состояние отклика сайта
        self.assertEqual(get_cat_fact(), 200)

    def test_status_code_dog(self): # тест кода состояние отклика другого сайта
        self.assertEqual(get_dog_fact(), 200)

    def test_translate(self): # тест перевода
        alphabet = set('abcdefghijklmnopqrstuvwxyz')
        text = 'I love my mother'
        trans_text = translate_fact(text)
        self.assertSetEqual(alphabet & set(trans_text), set())


if __name__ == '__main__':
    unittest.main()

