#!/usr/bin/python3
"""Minimum Operations python3 challenge"""


def minOperations(n):
    """ Calculates the fewest number of operations needed
    to result in exactly n H characters in this file.
    Returns:
        An integer. 0 if n is impossible to achieve
    """
    pasted_characters = 1 # number of characters in a file
    clipboard = 0 # number of H's copied
    counter = 0 # operations counter

    while pasted_characters < n:
        # if nothing was copied
        if clipboard == 0:
            # copy all
            clipboard = pasted_characters
            # increment operations counter
            counter += 1

        # if nothing was pasted
        if pasted_characters == 1:
            # paste
            pasted_characters += clipboard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted_characters # remaining chars to Paste

        # check if it is impossible by checking if the clipboard has
        # more than the needed to reach the number desired which
        # also means number of characters in the file is equal or
        # more than that in the clipboard.
        # It is impossible to achieve n of chars in both situations
        if remaining < clipboard:
            return 0

        # if it can't be divided
        if remaining % pasted_characters != 0:
            # paste current clipboard
            pasted_characters += clipboard
            # increment operations counter
            counter += 1
        else:
            # copy all
            clipboard = pasted_characters
            # paste
            pasted_characters += clipboard
            # increment operations counter
            counter += 2

        # if desired result is gotten
        if pasted_characters == n:
            return counter
        else:
            return 0
