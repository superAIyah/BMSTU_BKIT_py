from Lab3.lab3_package.gen_random import gen_random
# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

        if self.ignore_case:
            self.data = list(map(lambda s : str(s).lower(), items)) # приведение элементов к строке без учета регистра
        else:
            self.data = list(map(str, items)) # приведение элементов к строке с учетом регистра

        self.used_elements = set()
        self.index = 0
        pass

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index += 1
                if current not in self.used_elements: # возвращаем все эл-ты не встреющиеся ранее
                    self.used_elements.add(current)
                    return current
        pass

    def __iter__(self):
        return self

# Тестирование на примерах
print("TEST 1")
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
for elem in Unique(data):
    print(elem)
print("TEST 2")
data = gen_random(10, 1, 3)
for elem in Unique(data):
    print(elem)
print("TEST 3")
data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for elem in Unique(data):
    print(elem)
print("TEST 4")
for elem in Unique(data, ignore_case=True):
    print(elem)