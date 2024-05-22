#!/usr/bin/python3
"""UTF-8 Validation"""


#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    def count_of_bytes(n):
        """
        Get the plage number of a number in UTF-8
        """
        mask = 1 << 7
        i = 0
        while (n & mask):
            i += 1
            mask = mask >> 1
        return i

    count = 0        
    for i in data:
        if not count:
            count = count_of_bytes(i)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            count -= 1
            if count_of_bytes(i) != 1:
                return False
    return count == 0
