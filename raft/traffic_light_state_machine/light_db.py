# light.py

# initial state of the traffic light

Init = {
    'out1': 'G',
    'out2': 'R',
    'clock': 0,
    'pc': 'G1'
}

# define functions that determine state membership and state update
    # trick: Python `and` returns last value
    # >>> 2 & 3
    #     3

# in state G1, either clock is less than 30 -> update clock
# or clock=30, update color and reset clock to zero
G1 = lambda s: s['pc'] == 'G1' and (
               (s['clock'] < 30 and dict(s, clock=s['clock'] + 1))
            or (s['clock'] == 30 and dict(s,out1='Y', clock=0, pc='Y1'))
            )

Y1 = lambda s: s['pc'] == 'Y1' and (
            (s['clock'] < 5 and dict(s, clock=s['clock'] + 1))
            or (s['clock'] == 5 and dict(s, out1='R', out2='G', clock=0, pc="G3"))
            )

G2 = lambda s: s['pc'] == 'G2' and (
            (s['clock'] < 60 and dict(s, clock=s['clock'] + 1))
            or (s['clock'] == 60 and dict(s, out1='Y', clock=0, pc="Y2"))
            )

Y2 = lambda s: s['pc'] == 'Y2' and s['clock'] < 5 and dict(s, clock=s['clock'] + 1)

Next = G1 or Y1 or G2 or Y2

def run():
    s = Init
    while s:
        print(s)
        s = Next(s) # state transition

    # If here, there was no next state
    print("DEADLOCK. Traffic light stuck.")

run()

