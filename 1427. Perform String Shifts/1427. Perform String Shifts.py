"""
Answer to: https://leetcode.com/problems/perform-string-shifts/
"""
from typing import List
from functools import reduce


def solution_1(s: str, shift: List[List[int]]) -> str:
    """
    This is the optimal solution to the problem.
    It is O(n) time complexity and O(n) space complexity,
    where n is the length of the string. This is due to the use
    of the reduce function to calculate the total shift and the
    slicing operation, which creates a new string.

    Args:
        s (str): A string to shift.
        shift (List[List[int]]): A list of shifts to perform on the string. The first element
            of each list is a direction (0 for left, 1 for right), and the second element is
            the amount to shift.

    Returns:
        str: The string after performing all the shifts.
    """

    # Calculate the total shift. Shifting to the left is subtracting the amount,
    # and shifting to the right is adding the amount. The modulo operation is used
    # to handle cases where the total shift is greater than the length of the string.
    tot_shift = reduce(
        lambda tot, val: tot + (val[1] if val[0] else -val[1]), shift, 0
    ) % len(s)

    # Perform the shift on the string.
    return s[-tot_shift:] + s[:-tot_shift]
