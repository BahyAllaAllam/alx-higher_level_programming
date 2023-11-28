#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord('a'), ord('z')):
            i = ord(i) - 32
            print("{:c}".format(i), end="")
        else:
            print("{}".format(i), end="")
