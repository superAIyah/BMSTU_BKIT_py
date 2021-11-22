import operator
data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    print("TEST 1")
    result = list(zip(*sorted([(-x**2, x) for x in data], key=operator.itemgetter(0))))[1]
    print(*result)
    print("DATA")
    print(data)
    print("TEST 2")
    result_with_lambda = sorted(data, key=lambda x : -x**2)
    print(*result_with_lambda)