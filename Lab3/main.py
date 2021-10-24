from factory.detail import Detail
from factory.detprod import DetProd
from factory.producer import Producer

#Производители
prods = [
    Producer(1, "немецкая компания"),
    Producer(2, "строительный завод"),
    Producer(3, "китайский завод"),
    Producer(4, "авиационный завод"),
    Producer(5, "антиквариатная фабрика"),
]

#Детали
dets = [
    Detail(1, "айфон", 100, 3),
    Detail(2, "шасси", 50, 3),
    Detail(3, "антрeсоль", 10, 1),
    Detail(4, "двигатель", 80, 1),
    Detail(5, "кран", 10, 2),
]

dets_prods = [
    DetProd(2, 1),
    DetProd(4, 1),
    DetProd(1, 5),
    DetProd(3, 5),
    DetProd(3, 4),
    DetProd(3, 2),
    DetProd(5, 1),
    DetProd(5, 2),
    DetProd(5, 3),
    DetProd(5, 4),
    DetProd(5, 5),
]

def main():
    '''Основная функция'''

    #один ко многим
    one_to_many = [(p.name, d.name, d.price)
        for p in prods
        for d in dets
        if p.id == d.id_producer]

    #многие ко многим
    many_to_many = [(d.name, p.name)
        for p in prods
        for d in dets
        for dp in dets_prods
        if dp.det_id == d.id and dp.prod_id == p.id
    ]

    print("Задача 1")
    print("Вывести производителей, в которых есть слово \"завод\" и их детали")
    correct_prods = [elem[0] for elem in one_to_many if 'завод' in elem[0]]
    keys = [[] for i in range(len(correct_prods))]
    ans = dict(zip(correct_prods, keys))
    for p, d, _ in one_to_many:
        if p in ans:
            ans[p].append(d)
    print("Ответ:")
    for elem in ans:
        print(f"{elem} : {', '.join(ans[elem])}")
    print()
    print("Задача 2")
    print("Вывести производителей отсортированных по средней цене их деталей."
          " Среднюю цену округлить до двух знаков после запятой")
    print("Ответ:")
    prod_names = set(elem[0] for elem in one_to_many)
    mas = []
    for elem in prod_names:
        cnt = 0
        sum = 0
        for p, d, price in one_to_many:
            if p == elem:
                sum += price
                cnt += 1
        mas.append((elem, sum/cnt))
    mas = sorted(mas, key=lambda x: x[1])
    print(mas)
    for name, price in mas:
        print(f"{name} : {round(price, 2)}")
    print()
    print("Задача 3")
    print("Вывести все детали, начинающиеся на букву \"а\", "
          "а также их отделы")
    d = dict()
    for d_name, p_name in many_to_many:
        if d_name.startswith('а'):
            try:
                d[d_name].append(p_name)
            except:
                d[d_name] = []
                d[d_name].append(p_name)
    print("Ответ:")
    for elem in d:
        print(f"{elem} : {', '.join(d[elem])}")

if __name__ == '__main__':
    main()





