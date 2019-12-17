from collections import OrderedDict
import time
import threading
import colorama
from queue import Queue

# TODO: add client interactions. E.g., unscheduled button push.

class trafficLight:
    """Simulate a traffic light state machine."""

    def __init__(self):
        self.current_state = 'a'
        self.states = OrderedDict({'a': ('green', 'red', 10),
                    'b': ('yellow', 'red', 5),
                    'c': ('red', 'green', 20),
                    'd': ('red', 'yellow', 5)
                    })

        self.q = Queue()
        self.x_time = 0
        self.clock = 0

    def get_current_state(self):
        return self.current_state

    def get_ix(self, state):
        states_items = self.states.items()
        for ix,v in enumerate(states_items):
            if v[0] == state:
                return ix

    def get_current_ix(self):
        return self.get_ix(self.current_state)

    def print_state(self):
        """Print letter in formatted color based on state."""
        if self.current_state == 'a':
            print(colorama.Fore.GREEN + 'G', end=' ')
            print(colorama.Fore.RED + 'R')
            print(colorama.Fore.BLACK, end='')

        if self.current_state == 'b':
            print(colorama.Fore.YELLOW + 'Y', end=' ')
            print(colorama.Fore.RED + 'R')
            print(colorama.Fore.BLACK, end='')

        if self.current_state == 'c':
            print(colorama.Fore.RED + 'R', end=' ')
            print(colorama.Fore.GREEN + 'G')
            print(colorama.Fore.BLACK, end='')

        if self.current_state == 'd':
            print(colorama.Fore.RED + 'R', end=' ')
            print(colorama.Fore.YELLOW + 'Y')
            print(colorama.Fore.BLACK, end='')

    def get_next_state(self):
        states_items = list(self.states.items())
        if self.get_current_ix() + 1 == len(self.states):
            return states_items[0][0]
        else:
            next_state_data = states_items[self.get_current_ix() + 1]
            next_state = next_state_data[0]
            return next_state

    def start(self):
        while True:
            print(f"t: {self.x_time}", f"state: {self.current_state}", end=' ')
            self.print_state()
            # print(colorama.Fore.BLACK, end='')

            time.sleep(0.5)
            self.x_time += 1
            t1 = threading.Thread(target=self.change_state())
            t1.start()

    def change_state(self):
        if self.x_time >= 3:
            self.current_state = self.get_next_state()
            self.x_time = 0

            print(colorama.Fore.CYAN + 'state change!')
            print(colorama.Fore.BLACK, end='')


assert trafficLight().get_current_state() == 'a'
assert trafficLight().get_current_ix() == 0
assert trafficLight().get_next_state() == 'b'

if __name__ == "__main__":
    TL = trafficLight()
    print(f"TL: {TL}")