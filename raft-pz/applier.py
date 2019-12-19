"""
 “applier loop”

Client operations transition the machine from one state to another.
You should have a loop somewhere that takes one client operation at the time
(in the same order on all servers – this is where Raft comes in),
and applies each one to the state machine in order.
This loop should be the only part of your code that touches the application state (key/value mapping)


unique identifier for each client request,
so that you can recognize if you have seen,
and more importantly, applied, a particular operation in the past.

"""