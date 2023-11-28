#!/usr/bin/python3
def islower(c):
    if ord(c) in range(ord('a'), ord('z')):
        return True
    else:
        return False

def uppercase(str):
    for i in str:
        print("{:c}".format(ord(i)) if not islower(i) else ord(i) - 32, end="")
    print("")
