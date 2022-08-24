#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

positive_remainder = number % 10
negative_remainder = (abs(number) % 10) * -1

if number >= 0:
    if positive_remainder > 5:
        print(f"Last digit of {number} is {positive_remainder} and is greater than 5")
    elif positive_remainder == 0:
        print(f"Last digit of {number} is {positive_remainder} and is 0")
    else:
        print(f"Last digit of {number} is {positive_remainder} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {negative_remainder} and is less than 6 and not 0")
