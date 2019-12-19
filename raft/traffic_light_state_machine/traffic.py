from collections import OrderedDict, namedtuple
import time
import threading
import colorama
import itertools
import operator
# from queue import Queue
# TODO: add client interactions. E.g., unscheduled button push. Use queue pattern.

# time interval in seconds to fast-forward simulations
SLEEP_BEAT = 1

class trafficLight:
    """Simulate a traffic light state machine."""

    def __init__(self):

        # set up possible states
        self.State = namedtuple('State', ['stateName', 'out1', 'out2', 'time'])
        self.stateA = self.State('a', 'green', 'red', 5)
        self.stateB = self.State('b', 'yellow', 'red', 2)
        self.stateC = self.State('c', 'red', 'green', 5)
        self.stateD = self.State('d', 'red', 'yellow', 2)

        self.current_state = self.stateA.stateName
        self.states = [self.stateA, self.stateB, self.stateC, self.stateD] # preserve order

        self.state_change_times = [s.time for s in self.states]

        # self.q = Queue()
        self.x_time = 0
        self.clock = 0

    def get_current_state(self):
        return self.current_state

    def get_ix_from_name(self, state):
        state_names = [s.stateName for s in self.states]
        return state_names.index(state)

    def get_current_ix(self):
        return self.get_ix_from_name(self.current_state)

    def print_state(self):
        """Print letter in formatted color based on state."""
        if self.current_state == 'a':
            print(colorama.Fore.GREEN + 'G', end=' ')
            print(colorama.Fore.RED + 'R')
            print(colorama.Fore.BLUE, end='')

        if self.current_state == 'b':
            print(colorama.Fore.YELLOW + 'Y', end=' ')
            print(colorama.Fore.RED + 'R')
            print(colorama.Fore.BLUE, end='')

        if self.current_state == 'c':
            print(colorama.Fore.RED + 'R', end=' ')
            print(colorama.Fore.GREEN + 'G')
            print(colorama.Fore.BLUE, end='')

        if self.current_state == 'd':
            print(colorama.Fore.RED + 'R', end=' ')
            print(colorama.Fore.YELLOW + 'Y')
            print(colorama.Fore.BLUE, end='')

    def get_next_state(self):

        # check if current state is last in state machine cycle
        # if yes, cycle back to first State.stateName
        if self.get_current_ix() + 1 == len(self.states):
            return self.states[0].stateName

        # return stateName of subsequent element
        else:
            next_state = self.states[self.get_current_ix() + 1].stateName
            return next_state

    def start(self):
        while True:
            clock_format = str(self.clock).zfill(3)
            time_format = str(self.x_time).zfill(3)
            print(colorama.Fore.BLUE + f"clock: {clock_format}| t: {time_format} |", f"state: {self.current_state}", end=' ')
            self.print_state()

            time.sleep(SLEEP_BEAT)
            self.x_time += 1
            self.clock += 1
            t1 = threading.Thread(target=self.change_state())
            t1.start()

    def state_change_warning(self):
        print(colorama.Fore.CYAN + 'state change!')
        print(colorama.Fore.BLACK, end='')


    def change_state(self):

        # if state_change_times = [5, 2, 5, 2]
        # state_change_times_cumulative = [5, 7, 12, 14]

        times_accum = list(itertools.accumulate(self.state_change_times
                                                                  , operator.add))

        # change state if timer is at border time interval
        if self.x_time in times_accum:
            self.current_state = self.get_next_state()
            self.state_change_warning()

        # restart x_time after 1 full cycle
        if self.x_time >= sum(self.state_change_times):
            self.x_time = 0

# test initial state
assert trafficLight().get_current_state() == 'a'
assert trafficLight().get_current_ix() == 0
assert trafficLight().get_next_state() == 'b'

if __name__ == "__main__":
    TL = trafficLight()
    print(f"TL: {TL}")
    TL.start()

