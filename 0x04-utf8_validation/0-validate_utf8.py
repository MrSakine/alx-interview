#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    n_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for i in data:
        a = bin(i)[2:].zfill(8)
        if n_bytes == 0:
            for bit in a:
                if bit == '0':
                    break
                n_bytes += 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (i & mask1 and not (i & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
