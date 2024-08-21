#!/usr/bin/python3
""" Making Change module """
from typing import List


def makeChange(coins: List[int], total: int):
    """
    determine the fewest number of coins needed to meet a given amount total

    Args:
        - coins: list of the values of the coins in your possession
        - total: a given amount

    Return:
        - If total is 0 or less, 0
        - If total cannot be met by any number of coins you have, -1
    """
    if total <= 0:
        return 0

    return -1
