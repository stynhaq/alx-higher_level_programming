#!/usr/bin/python3

def islower(c):
    to_ascii = ord(c)

    if to_ascii >= 97 and to_ascii <= 122:
        return True
    return False
