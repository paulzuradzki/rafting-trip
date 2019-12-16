# problem: result may not be available yet
# use Event wait
# this is what a Future aims to solve

import threading
import time

class Result:
    def __init__(self):
        self.evt = threading.Event()
    def set_result(self, value):
        self.value = value
        self.evt.set()
    def get_result(self):
        self.evt.wait()
        return self.value


def func(x, y, result):
    time.sleep(3)
    result.set_result(x+y)

result = Result()
t = threading.Thread(target=func, args=(2,3,result))
t.start()

print(result.get_result())