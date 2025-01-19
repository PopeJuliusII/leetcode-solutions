"""
Answer to: https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""


def solution_1(s: str) -> int:
    """
    This is the optimal solution to the problem.
    The time complexity is O(n), where n is the length of the string.
    This is due to the for loop. The space complexity is O(1).

    Args:
        s (str): The string to split into balanced substrings.

    Returns:
        int: The maximum number of balanced substrings that can be created.
    """
    cnt = substrings = 0
    for char in s:
        cnt += 1 if char == "R" else -1
        # Create a substring when an equal number of R and L characters exist, greedily.
        substrings += not cnt
    return substrings
