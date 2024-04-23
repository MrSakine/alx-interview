#!/usr/bin/python3
"""
A function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n

    Attributes:
        n (any): integer

    Returns:
        - An empty list if n is less than or equal to zero
        - A list of lists of integers if n is greater than zero
    """
    if (n <= 0):
        return ([])
    result = list([] for _ in range(n))
    for i in range(0, n):
        temp = result[i]
        temp.append(1)
        counter = 0 if (i == 0) else len(result[i - 1])
        for j in range(0, counter):
            if (j + 1 < len(result[i - 1])):
                a = result[i - 1][j]
                b = result[i - 1][j + 1]
                temp.append(sum([a, b]))
            else:
                temp.append(1)
        result[i] = temp
    return (result)
