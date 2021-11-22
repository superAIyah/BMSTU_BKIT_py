goods = [                       # список словарей для теста
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title' : None, 'price' : 100, 'color' : 'white'},
    {'title' : None, 'price' : None, 'color' : None}
]

def field(items, *args):
    assert len(args) > 0
    key = args[0]
    if len(args) == 1:
        for dict in items: # последовательно выдаем значения полей
            if dict[key]:  # элемент не None
                yield dict[key]
    else:
        for dict in items: # фиксируем словарь
            res_dict = {}
            for key in args: # находим в нем все нужные ключи
                if dict[key]: # элемент не None
                    res_dict[key] = dict[key]
            if len(res_dict) != 0:
                yield res_dict # последовательно возвращаем нужный нам подсловарь
            res_dict.clear()

print('TEST 1')
for elem in field(goods, 'title'):
    print(elem)
print('TEST 2')
for elem in field(goods, 'title', 'price'):
    print(elem)
