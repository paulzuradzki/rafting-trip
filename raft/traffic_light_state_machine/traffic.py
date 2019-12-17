from collections import OrderedDict
from queue import Queue
import time

class trafficLight:

    def __init__(self):
        self.current_state = 'a'
        self.states = OrderedDict({'a': ('green', 'red', 30),
                    'b': ('yellow', 'red', 30),
                    'c': ('red', 'green', 30),
                    'd': ('red', 'yellow', 30)
                    })

        self.q = Queue()
        self.time = 0

    def get_current_state(self):
        return self.current_state

    def get_ix(self, state):
        states_items = self.states.items()
        for ix,v in enumerate(states_items):
            if v[0] == state:
                return ix

    def get_current_ix(self):
        return self.get_ix(self.current_state)

    def get_next_state(self):
        if self.get_current_ix() + 1 == len(self.states):
            return self.states[0]
        else:
            states_items = list(self.states.items())
            next_state_data = states_items[self.get_current_ix() + 1]
            next_state = next_state_data[0]
            return next_state

    def timer(self):
        while True:
            time.sleep(1)
            self.time += 1
            print(f"t: {self.time}", f"state: {self.current_state}")

    def change_state(self):
        self.current_state = self.get_next_state()


assert trafficLight().get_current_state() == 'a'
assert trafficLight().get_current_ix() == 0
assert trafficLight().get_next_state() == 'b'

if __name__ == "__main__":
    TL = trafficLight()
    print(f"TL: {TL}")




