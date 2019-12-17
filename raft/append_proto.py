# prototype raft append mechanism

log = [ ]

# def rappend(term=0,
#             leaderId=0,
#             prevLogIndex,
#             prevLogTerm,
#             entries: list = [{'key', ''}],
#             leaderCommit)
#             -> (term, success):
#
#     if term < currentTerm:
#         return False


def rappend(log, ix, entry):
    if ix > len(log):
        print(False)
        return False
    else:
        log.append(entry)
        print(True)
        return True



