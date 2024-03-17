"""
Answer to: https://leetcode.com/problems/valid-parentheses/
"""


def solution_1(s: str) -> bool:
    """
    This is the optimal solution to the problem.
    It has a time complexity of O(n) and a space complexity of O(n).
    This is due to iterating over the string and using
    a stack to store the opening parentheses, potentially
    storing every character in the string.

    Args:
        s (str): A string of parentheses to check for validity.

    Returns:
        bool: Whether the string of parentheses is valid.
    """
    inverse = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for char in s:
        # Append opening parentheses to the stack.
        if char in inverse:
            stack.append(char)

        # Check if the closing parentheses matches the last opening parentheses.
        elif not stack or inverse.get(stack.pop()) != char:
            return False

    # If the stack is not empty, there are unmatched opening parentheses.
    return not stack
