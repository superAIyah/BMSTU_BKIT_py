def print_result(funct):
    def wrapper():
        print(funct.__name__)
        res = funct()
        if isinstance(res, list):
            for elem in res:
                print(elem)
            return
        if isinstance(res, dict):
            for key, val in res.items():
                print(f'{key} = {val}')
            return
        print(res)
    return wrapper


@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()