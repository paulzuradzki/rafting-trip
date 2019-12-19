from collections import namedtuple
import logging
from pprint import pformat

logging.basicConfig(filename='app.log', filemode='w',
                    level=logging.DEBUG,
                    datefmt='%d-%b-%y %H:%M:%S',
                    format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')

class log():
    def __init__(self):
        self.entries = []
        self.current_term = 1

    def __len__(self):
        return len(self.entries)

    def __repr__(self):
        return f"log entries:\n{pformat(self.entries)}"

    def show_entries(self):
        for ix, e in enumerate(self.entries):
            print(f"ix: {ix}, entry: {e}")


    def append_entries(self, prev_ix, prev_term, entries):

        logging.info(f"BEFORE: \n{pformat(self.entries)}\n")

        # check if entries is empty

        if prev_ix != -1:
            try:
                self.entries[0]
                self.entries[prev_ix]
            except IndexError:
                logging.info("FALSE")
                return False


        # log empty when prev_ix=-1; append entries
        if prev_ix < 0 and len(self.entries) == 0:
            self.entries.extend(entries)
            logging.info("TRUE")
            logging.info(f"AFTER: \n{pformat(self.entries)}\n")
            return True

        # check term of prior index and that it matches supplied prev_term
        if self.entries[prev_ix].term != prev_term:
            logging.info("FALSE")
            logging.info(f"AFTER: \n{pformat(self.entries)}\n")
            return False

        # check if previous index equals supplied prev_ix
        if len(self.entries)-1 != prev_ix:
            logging.info("FALSE")
            logging.info(f"AFTER: \n{pformat(self.entries)}\n")
            return False

        for entry in entries:
            if entry.term < self.current_term:
                logging.info("FALSE")
                logging.info(f"AFTER: \n{pformat(self.entries)}\n")
                return False
            else:
                self.entries.append(entry)
                logging.info("TRUE")
                logging.info(f"AFTER: \n{pformat(self.entries)}\n")
                return True


    def test_append_entries(self):

        entry0 = Entry(term=1, entry='set x=1')
        entry1 = Entry(term=1, entry='set y=1')
        entry2 = Entry(term=1, entry='set y=9')
        entry3 = Entry(term=2, entry='set x=2')
        entry4 = Entry(term=3, entry='set x=0')
        entry5 = Entry(term=3, entry='set y=7')
        entry6 = Entry(term=3, entry='set x=5')
        entry7 = Entry(term=3, entry='set x=4')

        assert l.append_entries(0,1,[entry1]) == False # incorrect prev_ix
        assert l.append_entries(1,1,[entry1]) == False # incorrect prev_ix
        assert l.append_entries(-1,1,[entry0])
        assert l.append_entries(0,1,[entry1])
        assert l.append_entries(1,1,[entry2])
        assert l.append_entries(2,1,[entry3])
        assert l.append_entries(2,1,[entry3]) == False # entry already appended
        assert l.append_entries(2,2,[entry4]) == False # wrong prev_ix
        assert l.append_entries(3,2,[entry4])
        assert l.append_entries(2,1,[entry3]) == False # prior entry (entry4) is term 4
        assert l.append_entries(-1,1,[entry0]) == False # incorrect ix and self.entrie must be empty for prev_ix=-1
        assert l.append_entries(-1,1,[entry0]) == False # # incorrect ix and self.entrie must be empty for prev_ix=-1

        assert l.append_entries(4,3,[entry5])
        assert l.append_entries(5,3,[entry6])
        assert l.append_entries(6,3,[entry7])

class Server:
    pass

class Follower(Server):
    pass

class Leader(Server):
    pass

Entry = namedtuple('Entry', ['term', 'entry'])

if __name__ == "__main__":
    l = log()

    entry0 = Entry(term=1, entry='set x=1')
    entry1 = Entry(term=1, entry='set y=1')
    entry2 = Entry(term=1, entry='set y=9')
    entry3 = Entry(term=2, entry='set x=2')
    entry4 = Entry(term=3, entry='set x=0')
    entry5 = Entry(term=3, entry='set y=7')
    entry6 = Entry(term=3, entry='set x=5')
    entry7 = Entry(term=3, entry='set x=4')

    l.test_append_entries()

