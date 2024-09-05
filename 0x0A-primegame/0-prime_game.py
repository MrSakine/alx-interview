#!/usr/bin/python3
""" Prime game module """


def prime_number(n):
    """ Return prime numbers between 1 and n """
    primes = []
    is_prime = [True] * (n + 1)
    for num in range(2, n + 1):
        if is_prime[num]:
            primes.append(num)
            for i in range(num, n + 1, num):
                is_prime[i] = False
    return primes


def isWinner(x, nums):
    """
    Prime Game

    Args:
        - x is the number of rounds
        - nums is an array of n

    Returns:
        - name of the player that won the most rounds
        - If the winner cannot be determined, return None
    """
    if not x or not nums:
        return None

    maria_wins, ben_wins = 0, 0
    for round_limit in nums[:x]:
        prime_numbers = prime_number(round_limit)
        if len(prime_numbers) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"

    return None
