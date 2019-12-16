# kvclient.py

# Used by clients to access the KV store

from socket import *
import msgpass
import pickle

def encode_request(method, *args) -> bytes:
    # return the message
    return pickle.dumps((method, args))

def decode_result(msg:bytes):
    return pickle.loads(msg)

class KVStore:
    def __init__(self, address):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(address)

    # fancy way
    def __getattr__(self, method):
        def do_request(*args):
            msgpass.send_message(self.sock,
                                 encode_request(method, *args)
                                 )
            resp = msgpass.recv_message(self.sock)
            return decode_result(resp)
        return do_request

    # def get(self, key):
    #     msgpass.send_message(self.sock,
    #                          encode_request('get', key)
    #                          )
    #     resp = msgpass.recv_message(self.sock)
    #     return decode_result(resp)

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

