import zmq
context = zmq.Context()

sock = context.socket(zmg.REQ) # requestor
sock.connect("tcp://localhost:30000")
sock.send(b"Hello World")
resp = sock.recv()