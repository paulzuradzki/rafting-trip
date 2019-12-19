import log

class Server:
    def __init__(self):

        # persistent state
        self.log = log.log()
        self.current_term = None
        self.voted_for = None

        # volatile state
        self.commit_ix = None
        self.last_applied = None

class Leader(Server):
    def __init__(self):
        super().__init__()

        self.follower_meta = follower_meta(self)

    # def append_entries_rpc(self, follower):
    #
    #     # get zero-index of second to last item
    #     prev_ix = len(self.log.entries)-2
    #     follower.log.append_entries(prev_ix, 1, [self.log.entries[prev_ix + 1]])
    #
    #     if not success_flag:
    #         self.append_entries(follower):
    #             success_flag = follower.log.append_entries(prev_ix-1, 1, [self.log.entries[prev_ix]])
    #
    #     return success_flag

class follower_meta:
    def __init__(self, leader):
        self.next_ix = len(leader.log.entries) - 1  # zero-indexed; init to log index + 1
        self.match_ix = 0
        self.prev_ix = len(leader.log.entries) - 2

        # term of last entry in log; this is the assumed prev_term for follower when leader appends entry
        try:
            self.prev_term = leader.log.entries[-1].term
        except: 1

class Follower(Server):
    pass

entry0 = log.Entry(term=1, entry='set x=1')
entry1 = log.Entry(term=1, entry='set y=1')
entry2 = log.Entry(term=1, entry='set y=9')
entry3 = log.Entry(term=2, entry='set x=2')
entry4 = log.Entry(term=3, entry='set x=0')
entry5 = log.Entry(term=3, entry='set y=7')
entry6 = log.Entry(term=3, entry='set x=5')
entry7 = log.Entry(term=3, entry='set x=4')

s0 = Leader()
# s0.log.append_entries(-1, 1, [entry0])
s0.log.append_entries(-1, 1, [entry0, entry1, entry3])
# s0.log.append_entries(2, 2, [entry4])

s1 = Follower()
# s0.append_entries_rpc(s1)

