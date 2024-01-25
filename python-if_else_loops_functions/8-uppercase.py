#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            upper = chr(ord(i) - 32)
            print("{}".format(upper), end="")
        else:
            print("{}".format(i), end="")
    print("")
