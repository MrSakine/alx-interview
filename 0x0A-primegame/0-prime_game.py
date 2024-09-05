#!/usr/bin/python3
""" Prime game module """


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
    def sieve_of_eratosthenes(n):
        """ sieve algorithm """
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        return sieve

    primes = sieve_of_eratosthenes(x)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[2:n+1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
