class Spam:
    def __getattr__(self, meth):
        print("Getting", meth)

"""
>>> s = Spam()
>>> s.foo
Getting foo
>>> s.blah
Getting blah
>>> s.whatever
Getting whatever

"""
