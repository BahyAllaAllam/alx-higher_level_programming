#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    if num_args != 0:
        print("{} arguments:".format(num_args))
    else:
        print("{} arguments:".format(0))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
