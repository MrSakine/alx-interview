#!/usr/bin/python3
""" Making Change module """
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        - coins: List of the values of the coins in your possession.
        - total: The total amount to achieve with the given coins.

    Return:
        - If total is 0 or less, return 0.
        - If total cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
            if amount == total and dp[amount] != float('inf'):
                return dp[amount]
    return dp[total] if dp[total] != float('inf') else -1
