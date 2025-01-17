"""
Answer to: https://leetcode.com/problems/smallest-even-multiple/
"""


def solution_1(n: int) -> int:
    """
    This is the optimal solution to the problem.
    Both time complexity and space complexity are O(1).
    If the number is even, return the number.
    Otherwise, return the smallest even multiple of the number.

    Args:
        n (int): The number.

    Returns:
        int: The smallest even multiple of the number.
    """
    return n * 2 if n % 2 else n
