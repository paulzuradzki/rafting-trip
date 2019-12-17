
"""

server
logentry


servertest
coodr


timekeeper
    get current server time (seconds)

server

    start
    stop

    config: how many servers there are; which server are we
        past list of server instance #s; don't count on continous numbering
    config timeout

    server shared properties -- holds shared properties that may exist
        beyond instance of server; can be called back

        config

    set time keeper
    get commit index (cluster)
    set commit index (cluster) - for testing, record that cluster has committed up through index

    get last index (server)
    set last index (server) - ""

    get next index
    get match index

    is voting member

    get cluster leader id
    get election timeout

    setOnReceiveMessageCallback





cluster config
    instances: {2, 5, 6, 7, 11}

command
    key, val

message class

Iserver (public interface)
    config
    election state: follower, candidate, leader
    min election timeout
    max election timeout
    heartbeat interval
    rpc timeout
    event
        sendmessage
            receiver ID
            serialized msg
        leadership change
            leader ID
            term
        election state
            term
            election state - server is follower, candidate, or leader
            voted this term
        apply config
            new cluster config
        commit config
            new single server config commited
            logindex
        snapshot installed
            last included index
            json: history of commands up through index
        caught up to leader; commit index reach last index of leader
    event handler - take event published by server and delegate

    receive message - called anytime server receives message from another server in cluster

    append log entry; reply back




ILog
    last index
    last term

    get term at index
    discard log entries after index
    commit

IPersistent
    current term
    voted for
    voted this term


LogEntry - abstract type (json, string, pickle)
    base class; contains properties directly related to algo;
        meant to be sub-classed in order to hold actual server state that is different

    command factory
    term - when entry received by leader
    key, value
    operator
    determine command type
    check if log entry is equal to another



project struct
    Iserver
    server
    LogEntry
    TimeKeeper

test
    actual config = get_config; backdoor; public interface matches private attributes
        check instance numbers group
        check self instance number

    election_after_proper_timeout
    one vote per server per election
    leader has majority vote
    leader has max term and committed logs





"""


class ServerState:
    def __init__(self):
        self.currentTerm = None
        self.votedFor = None
        self.log = { }

        self.commitIndex = None
        self.lastApplied = None


class LeaderState(ServerState):
    def __init__(self):
        super().__init__(self)