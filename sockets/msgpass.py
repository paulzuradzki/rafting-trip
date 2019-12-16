# msgpass.py

# Send a message.
# The message stays intact at all times.
# No partial messages or fragments.

def send_message(sock, msg):
    send_size(sock, len(msg))
    sock.sendall(msg)

def recv_message(sock):
    sz = recv_size(sock)
    msg = recv_exactly(sock, sz)
    return msg


def send_size(sock, sz: int):
    sock.sendall(sz.to_bytes(8, "big"))

def recv_size(sock):
    msg = recv_exactly(sock, 8)
    return int.from_bytes(msg, "big")

def recv_exactly(sock, nbytes):
    '''
    Receive exactly nbytes of data on a socket
    '''
    msg = b''
    while nbytes > 0:
        chunk = sock.recv(nbytes) # might return partial data
        if not chunk:
            raise IOError("Connection closed")
        msg += chunk
        nbytes -= len(chunk)
    return msg

