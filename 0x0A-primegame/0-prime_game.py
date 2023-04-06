#!/usr/bin/python3
"""
Solution to the Prime game problem
"""


def isWinner(x, nums):
    """
    Find winner of the prime game
    Args:
        x   : number of rounds
        nums: array of n
    Return:
        Name of player that won most rounds
    """
    # returning None if winner cannot be determined
    if x is None or x == 0 or nums is None or nums == []:
        return None
    
    Maria = 0
    Ben = 0
    for iter in range(x):
        prime = prime_numbers(nums[iter])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Ben > Maria:
        return "Ben"
    elif Maria > Ben:
        return "Maria"

def prime_numbers(n):
    """
    Return prime numbers between 1 and n
    Args:
        n : range upper bound, range lower bound is always 1
    """
    prime = []
    bridge = [True] * (n + 1)
    
    for iter in range(2, n + 1):
        if (bridge[iter]):
            prime.append(iter)
            for iterator in range(iter, n + 1, iter):
                bridge[iterator] = False
    return prime