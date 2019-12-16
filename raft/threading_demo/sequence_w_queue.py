# sequence threads and have them communicate via queues

import threading
import queue
q = queue.Queue()

def consumer():
    while True:
        item = q.get() # get item
        print("Got:", item)

threading.Thread(target=consumer).start()

q.put('hello')

q.put('world')