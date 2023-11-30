#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide
    a = 10
    b = 5
    addition = add(a, b)
    subtraction = subtract(a, b)
    multiplication = multiply(a, b)
    division = divide(a, b)
    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, subtraction))
    print("{} + {} = {}".format(a, b, multiplication))
    print("{} + {} = {}".format(a, b, division))
