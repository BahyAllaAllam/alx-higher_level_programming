#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1
    if num_args > 1:
        print("{} arguments:".format(num_args))
    elif num_args == 1:
        print("1 argument:")
    else:
        print("0 arguments.")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
