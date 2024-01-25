#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            upper = chr(ord(i) - 32)
            result += "{}".format(upper)
        else:
            result += "{}".format(i)
    print(result)
