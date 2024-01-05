#!/usr/bin/python3
"""
Defining an empty class Ractangle
"""


import sys


def nqueens(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    solutions = 0
    for i in range(n):
        solutions += nqueens(n-1)
    return solutions


def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: python nqueens.py [N]')
        sys.exit(1)

    n = int(args[0])
    result = nqueens(n)
    print(result)


if __name__ == "__main__":
    main()
