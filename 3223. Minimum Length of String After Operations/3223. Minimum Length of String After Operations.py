"""
Answer to: https://leetcode.com/problems/minimum-length-of-string-after-operations/
"""
from collections import Counter


def solution_1(s: str) -> int:
    """
    This is the optimal solution to the problem.
    It is O(n) time complexity and O(1) space complexity,
    where n is the length of the list of numbers. This is due
    to the use of a single for loop to iterate through the list
    and the use of a fixed-size list to store the counts of each
    character.

    Args:
        s (str): A string to perform operations on.

    Returns:
        int: The minimum length of the string after the operations.
    """
    cnt_list = [0] * 26
    for c in s:
        # ord('a') = 97
        cnt_list[ord(c) - 97] += 1
    return sum(1 if cnt % 2 else 2 for cnt in cnt_list if cnt)


def solution_2(s: str) -> int:
    """
    This is the optimal solution to the problem.
    It is O(n) time complexity and O(1) space complexity,
    where n is the length of the list of numbers. The complexity
    is equivalent to solution_1, but this solution uses Counter.

    Args:
        s (str): A string to perform operations on.

    Returns:
        int: The minimum length of the string after the operations.
    """
    return sum(1 if cnt % 2 else 2 for cnt in Counter(s).values() if cnt)
