"""
Answer to: https://leetcode.com/problems/score-of-a-string/
"""


def solution_1(s: str) -> int:
    """
    This is the optimal solution to the problem.
    The time complexity of this solution is O(n) where n is the length of the string.
    This is because of the iteration over the string.
    The space complexity of this solution is O(1) because only constant space is used,
    i.e. the score variable and the for loop variable.

    Args:
        s (str): A string to process.

    Returns:
        int: The score of the string; the sum of the absolute differences of adjacent characters.
    """
    return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))
