from cm_timer import *
from unique import *
from gen_random import *
import json

def print_result(funct):
    def wrapper(arg):
        print(funct.__name__)
        res = funct(arg)
        if isinstance(res, list):
            for elem in res:
                print(elem)
            return res
        if isinstance(res, dict):
            for key, val in res.items():
                print(f'{key} = {val}')
            return res
        return res
    return wrapper

path = 'data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария
with open('data_light.json') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(Unique([x['job-name'].lower() for x in arg]))

@print_result
def f2(arg):
    return list(filter(lambda x : x.startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x : x + 'с опытом Python', arg))

@print_result
def f4(arg):
    return list(zip(arg, [rnd for rnd in gen_random(len(arg), 100_000, 200_000)]))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
