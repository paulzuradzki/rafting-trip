# How to make a thread wait for something using Events
# events have one-time use

import threading

x_event = threading.Event()

def func():
    print("waiting")
    x_event.wait()
    print("Done waiting")

threading.Thread(target=func).start()

print(x_event)

x_event.set()