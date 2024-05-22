#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    for i in data:
        a = str(bin(i)[2:].zfill(8))
        if int(a[0]) == 0:
            continue
        else:
            return False
    return True
