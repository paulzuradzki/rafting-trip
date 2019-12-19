# state_machine.py
"""
Updted on stable storage before responding to RPCs.
"""
class State:
    def __init__(self):
        self.current_term = None
        self.voted_for = None
        self.log = None
        self.commit_ix = None
        self.last_applied = None
        self.next_ix = None
        self.match_ix = None
