import zmq
ocntext = zmq.Context()
sock = context.socket(zmq.REP) # reply socket
sock.bind('tcp://*:30000')
msg = sock.recv()


# >>> msg
# >>> sock.send(b'Hey there')