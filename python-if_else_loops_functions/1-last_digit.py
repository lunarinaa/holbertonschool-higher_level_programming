#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_str = str(number)[-1]
last = int(last_digit_str)
if number < 0:
    last = -last
print(f"Last digit of {number} is {last} and is", end=" ")
if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
else:
    print("less than 6 and not 0")
