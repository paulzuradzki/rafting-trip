# echoclient.py

from socket import *

def echo_client(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)
    while True:
        data = input("message > ")
        msg = data.encode('utf-8')
        sock.sendall(msg)
        nrecv = len(msg)
        response = b''
        while nrecv > 0:
            part = sock.recv(nrecv)
            if not part:
                print('Connection closed!')
                return
            response += part
            nrecv -= len(part)
        print('response:', response)

if __name__ == '__main__':
    echo_client(('localhost', 25000))



