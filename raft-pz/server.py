from ..log import log

class Server:
    def __init__(self):
        self.log = log()

class Follower(Server):
    pass

class Leader(Server):
    pass

s0 = Server()