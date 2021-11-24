import time, sys
from contextlib import contextmanager

class cm_timer_1:
    def __init__(self):
        return
    def __enter__(self):
        self.time = time.time()
        return self.time
    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            print(f'{time.time() - self.time:.2f}')

@contextmanager
def cm_timer_2():
    start = time.time()
    yield
    print(f'{time.time() - start:.2f}')
if __name__ == '__main__':
    with cm_timer_1() as obj:
        time.sleep(5.5)

    with cm_timer_2() as obj:
        time.sleep(5.5)