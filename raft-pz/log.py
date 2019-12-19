
from collections import defaultdict
class Server:
    def __init__(self):
        self.log = []

    def get_log(self):
        return self.log

        return term, success

class Leader(Server):
    def __init__(self):
        self.leader_id = 's1'
        self.commit_ix = None
        self.follower_log_info = defaultdict(dict)

    follower_log_info = ''

    def append_entry(self,
                     term,
                     leader_id,
                     prev_log_ix,
                     prev_log_term,
                     entries,
                     leader_commit):
        term = None
        success = None

class Follower(Server):
    def __init__(self):
        # super().__init__.log = []
        self.prev_log_ix = 0
        self.prev_term = 0
        self.current_term = 1
        self.commit_ix = 1

    def set_log(self, log=None):
        self.log = log

    def append_entry(self, entry=None, ix=None, term=None, prev_log_term=None, prev_log_ix=None):

        success = None
        # Figure 2, step 1
        # (5.1)
        # reply false if term < current_term
        if term < self.current_term:
            success = False

        # Figure 2, step 2
        # (5.3)
        # reply false if log doesn't contain an entry at prev_log_index
        # whose term matches pre_log_term
        if self.log[prev_log_ix].term != prev_log_term:
            success = False

        # Figure 2, step 3
        # (5.3)
        # if an existing entry conflicts with a new one (same index but different terms)
        # , delete the existing entry and all that follow
        for entry in self.log:
            if entry.ix == ix and entry.term != term:
                conflict_ix = self.log.index(entry)
                self.log.set_log(self.log[:conflict_ix]) # delete step

        # Figure 2, step 4
        # Append any new entries not already in the log
        if entry not in self.log:
            print("Entry is not in log")
            self.log.append(entry)
            success = True
            return term, success

        # Figure 2, step 5
        # If leader_commit > commit_ix, set commit_ix = min(leader_commit, index of last new entry)
        if ix > self.commit_ix:
            self.commit_ix = min(ix, entry.ix)

        return self.current_term, success

class messageRPC:
    pass

class appendEntriesRPC(messageRPC):
    def __init__(self, term, leader_id, prev_log_ix, entries, leader_commit):
        self.term = term
        self.leader_id = leader_id
        self.prev_log_ix = prev_log_ix
        self.entries = entries
        self.leader_commit = self.leader_commit

# s0 = Leader()
# s1 = Follower()
# s2 = Follower()
# s3 = Follower()
# s4 = Follower()

from collections import namedtuple
import pprint


class log_entry:
    def __init__(self):
        self.term = None
        self.command = None
        self.committed = None
        self.msg_id = None

    def get_term(self):
        return self.term
    def get_command(self):
        return self.command
    def get_committed(self):
        return self.committed
    def get_msg_id(self):
        return self.msg_id

    def set_term(self, term=None):
        self.term = term
    def set_command(self, command=None):
        self.command = command
    def set_committed(self, committed=None):
        self.committed = committed
    def set_msg_id(self, msg_id):
        self.msg_id = msg_id

Entry = namedtuple('Entry', ['term', 'ix', 'command', 'committed', 'msg_id'])
entry0 = Entry(1,0,'set x=1', False, 'e1')
entry1 = Entry(1,1,'set y=1', False, 'e2')
entry2 = Entry(1,2,'set y=9', False, 'e3')
entry3 = Entry(2,3,'set x=2', False, 'e4')
entry4 = Entry(3,4,'set x=0', False, 'e5')
entry5 = Entry(3,5,'set y=7', False, 'e6')
entry6 = Entry(3,6,'set x=5', False, 'e7')
entry7 = Entry(3,7,'set x=4', False, 'e8')

# entry0 = 'a'
# entry1 = 'b'
# entry2 = 'c'

s0 = Leader()
s0.log = [entry0, entry1, entry2]

s1 = Follower()
s1.log = [entry0, entry1]

s2 = Follower()
s2.log = []

term, success = s1.append_entry(entry=entry2, ix=entry2.ix, term=entry2.term,
                                prev_log_term=1, prev_log_ix=1)

pprint.pprint(s1.log)
# s1.catchup_to_leader