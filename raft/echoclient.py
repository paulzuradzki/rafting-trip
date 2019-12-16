# echoclient.py

from socket import *
import msgpass

def echo_client(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)
    while True:
        data = input("message > ")
        msg = data.encode('utf-8')
        msgpass.send_message(sock, msg)
        response = msgpass.recv_message(sock)
        print('response:', response)

if __name__ == '__main__':
    echo_client(('localhost', 25000))



