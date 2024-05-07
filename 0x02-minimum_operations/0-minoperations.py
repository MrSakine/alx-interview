#!/usr/bin/python3
"""0-minoperations.py"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file
    """
    min_ops = 0
    div = 2
    while (isinstance(n, int) and n > 1):
        while (n % div):
            div += 1
        min_ops += div
        n = n // div
    return min_ops
