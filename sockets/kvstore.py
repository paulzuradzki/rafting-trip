# kvstore.py

# A networked Python dictionary

data = {}

def get(key):
    return data[key]

def set(key, value):
    data[key] = value

def delete(key):
    del data[key]


