# demo thread switches and race conditions

import threading

def incr():
    global x
    x = x + 1

def decr():
    global x
    x = x - 1

def spin(n, func):
    while n > 0:
        func()
        n -= 1

x = 0

spin(1_000_000, incr)
spin(1_000_000, decr)

t1 = threading.Thread(target=spin, args=(1_000_000, incr))
t2 = threading.Thread(target=spin, args=(1_000_000, decr))

t1.start(); t2.start()

print(x)



"""
prz-mbp:threading_demo pzuradzki$ python3 -i race_condition.py
>>> import dis
>>> dis.dis(incr)
  5           0 LOAD_GLOBAL              0 (x)
              2 LOAD_CONST               1 (1)
              4 BINARY_ADD
              6 STORE_GLOBAL             0 (x)
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
>>> dis.dis(decr)
  9           0 LOAD_GLOBAL              0 (x)
              2 LOAD_CONST               1 (1)
              4 BINARY_SUBTRACT
              6 STORE_GLOBAL             0 (x)
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
"""