#!/usr/bin/pythone3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        maximum = my_list[0]
        for num in my_list:
            if num > maximum:
                num = maximum
        return maximum
