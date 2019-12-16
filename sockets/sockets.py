from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.bind(('', 24000))
s.listen()
client, addr = s.accept()

