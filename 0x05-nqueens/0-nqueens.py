#!/usr/bin/python3
""" N queens """
from sys import argv, exit


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    elif not argv[1].isnumeric():
        print('N must be a number')
        exit(1)
    N = int(argv[1])
    if N < 4:
        print('N must be at least 4')
        exit(1)
