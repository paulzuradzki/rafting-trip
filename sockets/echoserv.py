from socket import *
from msgpass import send_message

def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    print("Server running at", address)
    while True:
        client, addr = sock.accept()
        print("Connection from", addr)
        echo_handler(client)


def echo_handler(client):
    while True:
        data = client.recv(10000)
        if not data:
            break
        client.sendall(data)
    print("Connection closed")
    client.close()

if __name__ == '__main__':
    echo_server(('', 25000))

