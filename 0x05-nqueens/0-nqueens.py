#!/usr/bin/python3
"""N-Queens Challenge"""

import sys

def print_usage_and_exit(message):
    print(message)
    sys.exit(1)

def is_safe(queens, row, col):
    """Check if placing a queen at (row, col) is safe from attacks."""
    for r, c in queens:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True

def solve_nqueens(n, row=0, queens=[]):
    """Recursively solve the N-Queens problem and collect solutions."""
    if row == n:
        print(queens)
        return
    
    for col in range(n):
        if is_safe(queens, row, col):
            solve_nqueens(n, row + 1, queens + [[row, col]])

def main():
    # Check for correct number of arguments
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    
    # Parse the size of the board
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")
    
    # Check for minimum size of the board
    if n < 4:
        print_usage_and_exit("N must be at least 4")
    
    # Solve the N-Queens problem
    solve_nqueens(n)

if __name__ == "__main__":
    main()
