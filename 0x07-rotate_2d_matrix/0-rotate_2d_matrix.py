#!/usr/bin/python3
"""0-rotate_2d_matrix.py"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D matrix 90 degrees clockwise
    """
    n = len(matrix)
    for lst in range(n // 2):
        f = lst
        lst = n - 1 - lst
        for i in range(f, lst):
            o = i - f
            top = matrix[f][i]
            matrix[f][i] = matrix[lst - o][f]
            matrix[lst - o][f] = matrix[lst][lst - o]
            matrix[lst][lst - o] = matrix[i][lst]
            matrix[i][lst] = top
    return matrix
