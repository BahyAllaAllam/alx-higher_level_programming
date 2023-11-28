#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(ord('a'), ord('z')):
            i = ord(i) - 32
            print("{:c}".format(i), end="" if chr(i) != str[-1] else "\n")
        else:
            print("{:c}".format(i), end="" if chr(i) != str[-1] else "\n")
