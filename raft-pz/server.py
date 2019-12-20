import log
import config

class Server:
    def __init__(self, id=None, address=None):

        self.id = id
        self.address = address

        # persistent state
        self.log = log.log()
        self.current_term = None
        self.voted_for = None

        # volatile state
        self.commit_ix = None
        self.last_applied = None

    def get_peers(self) -> list:
        peers = [s for s in SERVER_LIST if s != self]

        return peers

    def become_leader(self):

        # I'm sorry future me...
        self.__class__ = Leader

        # for s in self.get_peers():
        #     self.next_ix[s] = len(self.log)
        #     self.match_ix = 0
        #     self.prev_ix = len(self.log) - 1
        #     self.prev_term = 1

class Leader(Server):
    def __init__(self, id=None, address=None):
        super().__init__()

        # leader stores follower metadata
        self.next_ix =   {}
        self.match_ix =  {}
        self.prev_ix =   {}
        self.prev_term = {}
        self.become_leader()

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

SERVER_LIST = [Server(id=k, address=v) for k, v in config.SERVERS.items()]
s0 = SERVER_LIST[0]
peers = s0.get_peers()

# s0.log.append_entries(-1, 1, [entry0])
s0.log.append_entries(-1, 1, [entry0, entry1, entry3])
# s0.log.append_entries(2, 2, [entry4])

# s1 = Follower()
# s0.append_entries_rpc(s1)


