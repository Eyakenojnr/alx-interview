#!/usr/bin/python3
"""
Define isWinner function, a solution to the Prime Game problem
"""


def sieve_of_eratosthenes(n):
    """
    Precompute the list of primes up to n using the Sieve of Eratosthenes.
    Args:
        n (int): upper boundary of the range.
    Returns:
        list: A boolean list where True indicates a prime number.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve


def count_primes_up_to(n, sieve):
    """
    Count the number of primes up to n using a precomputed sieve.
    Args:
        n (int): Upper limit of range.
        sieve (list): Precomputed sieve of prime numbers.
    Returns:
        int: Count of prime numbers up to n.
    """
    return sum(sieve[:n + 1])


def isWinner(x, nums):
    """
    Determines winner of Prime Game.
    Args:
        x (int): Number of rounds of the game.
        nums (list): Upper limits of ranges for each round.
    Returns:
        str: Name of the winner ("Maria" or "Ben") or None if there's no winner.
    """
    if not x or not nums:
        return None

    max_num = max(nums)
    sieve = sieve_of_eratosthenes(max_num)

    Maria = Ben = 0
    for num in nums:
        prime_count = count_primes_up_to(num, sieve)
        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
