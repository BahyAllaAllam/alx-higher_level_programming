#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    if n < 0 or n >= len(str):
        return str
    for i in range(len(str)):
        if i != n:
            newstr += str[i]

    return newstr
