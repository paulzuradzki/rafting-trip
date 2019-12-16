# kvclient.py

# Used by clients to access the KV store

from socket import *
import msgpass
import pickle

def encode_request(method, *args) -> bytes:
    # return the message
    return pickle.dumps((method, args))

def decode_result(msg):
    return pickle.loads(msg)

class KVStore:
    def __init__(self, address):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(address)

    def get(self, key):
        msgpass.send_message(self.sock,
                             encode_request('get', key)
                             )
        resp = msgpass.recv_message(self.sock)
        return decode_result(resp)

    def set(self, key, value):
        msgpass.send_message(self.sock,
                             encode_request('set', key, value)
                             )
        resp = msgpass.recv_message(self.sock)
        return decode_result(resp)

    def delete(self, key):
        msgpass.send_message(self.sock,
                             encode_request('delete', key)
                             )
        resp = msgpass.recv_message(self.sock)
        return decode_result(resp)

"""
kvStore = KVStore('localhost')
kvStore.set('a', '1')
"""
