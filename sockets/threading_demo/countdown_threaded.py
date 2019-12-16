import time
import threading


def countdown(n):
    while n > 0:
        print('T-minus', n)
        time.sleep(5)
        n -= 1


t = threading.Thread(target=countdown, args=(5,))

t.start()

