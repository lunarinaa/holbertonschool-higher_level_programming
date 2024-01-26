#!/usr/bin/python3

def multiple_returns(sentence):
    tuple = ()
    if sentence[0] == 0:
        return None
    else:
        return len(sentence), sentence[0]
    return tuple
