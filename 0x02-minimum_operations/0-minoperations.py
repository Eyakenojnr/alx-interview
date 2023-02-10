#!/usr/bin/python3

"""Minimum Operations python3 challenge"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in this file.

    Return: 
        Integer. 0 if n is impossible to achieve.
    """
    pasted_characters = 1 # no. of characters in the file
    clipboard = 0 # no. of H's copied
    counter = 0

    while pasted_characters < n:
        # if nothing was copied
        if clipboard == 0:
            # copy all
            clipboard = pasted_characters
            # increment counter
            counter += 1

        # if nothing was pasted
        if pasted_characters == 1:
            # paste
            pasted_characters += clipboard
            # increment counter
            counter += 1
            # continue to nect loop
            continue

        remaining = n - pasted_characters # remaining chars to paste

        # Check if it is impossible by checking if clipboard has
        # more characters than needed to reach the number desried
        # which also means number of characters in file is equal
        # or more in the clipboard.
        # It is impossible to achieve n of chars in both situations
        if remaininf < clipboard:
            return 0

        # if it can't be divided
        if remaining % pasted_characters != 0:
            # paste current clipboard
            pasted_characters += clipboard
            # increment counter
            counter += 1
        else:
            # copy all
            clipboard = pasted_characters
            # paste
            pasted_characters += clipboard
            # increment counter
            counter += 2

    # if desired result is found
    if pasted_characters == n:
        return counter
    else:
        return 0
