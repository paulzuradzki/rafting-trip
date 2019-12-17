# raftnet.py

import msgpass
import raftconfig
import queue
from socket import *
import threading



class RaftNetwork:
    def __init__(self, myself):
        self.self_address = myself
        self.inbox = queue.Queue()
        self.socks = { }

    def send(self, dest, msg):
        '''
        Send a message to another server in the cluster
        '''
        # if not connected, try to  connect. Then send.
        # Maybe keep a cache of active connections
        if dest not in self.socks:
            self.socks[dest] = socket(AF_INET, SOCK_STREAM)
            self.socks[dest].connect(raftconfig.SERVERS[dest])
        msgpass.send_message(self.socks[dest], msg)

class RaftServer:
    def __init__(self, net):
        self.inbox = queue.Queue()
        self.net = net

    def run_server(self):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(raftconfig.SERVERS[self.address])
        sock.listen(1)
        while True:
            client, addr = sock.accept()
            threading.Thread(target=self.get_messages, args=(client,)).start()

    def recv(self):
        '''
        Receive a message from any other server
        '''

        return self.inbox.get()


# Thoughts: how can you test this?
#           can you make a "fake" network that operates "in process"

# node0 = RaftNetwork(0)
# node1 = RaftNetwork(1)
# node2 = RaftNetwork(2)
# node0.send(1, b'hello')
# msg = node1.recv()
# assert msg == b'hello'
#

