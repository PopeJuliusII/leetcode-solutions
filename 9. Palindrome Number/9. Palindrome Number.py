"""
Answer to: https://leetcode.com/problems/palindrome-number/
"""


def solution_1(x: int) -> bool:
    """
    This is the optimal solution to the problem.
    It is O(log10(x)) time complexity and O(1) space complexity.
    This is due to x being trimmed in the while loop and
    the use of a single integer to store the inverse of half of x.

    Args:
        x (int): The number to check whether it is a palindrome.

    Returns:
        bool: Whether the number is a palindrome.
    """
    # A value being a multiple of ten messes up the logic of the solution,
    # and, definitionally, cannot be a palindrome unless it is zero.
    if not x % 10:
        return not x

    # This will house half of the digits of x, from the end, in reverse.
    inverse: int = 0

    # For a palindrome, this while loop will create two numbers of the same length.
    while x > inverse:
        inverse: int = inverse * 10 + x % 10

        # This is required to handle odd-length numbers.
        # The middle digit will not be removed from x, as it has already been added to inverse.
        if x > inverse:
            x //= 10

    # If the number is a palindrome, x will be equal to inverse.
    # Note that negative numbers cannot be palindromes, as the negative sign is not a digit.
    # This solution will return False for negative numbers, as inverse cannot drop below zero,
    # ans so will never be equal to x.
    return x == inverse


def solution_2(x: int) -> bool:
    """
    This is the intuitive solution to the problem.
    It isn't necessarily the optimal solution, but it is a valid solution, as
    time and space complexity are rarely a concern for this problem.
    The time complexity is O(log(n) ** 2), where n is the number of digits in x.
    This is due to the implementation of the "str" function in Python, which is outlined here:
    https://github.com/python/cpython/blob/a03a09e068435f47d02649dda93988dc44ffaaf1/Objects/longobject.c#L1744
    The other operations, specifically the equality check and the reverse,
    have a time complexity of O(m), where m is the number of characters in string_x.
    Overall, this yields a time complexity of O(log(n) ** 2 + 2m);
    dropping the constant and lower order terms, yields O(log(n) ** 2).
    The space complexity is O(1) as no additional space is used.

    Args:
        x (int): The number to check whether it is a palindrome.

    Returns:
        bool: Whether the number is a palindrome.
    """
    string_x: str = str(x)
    return string_x == string_x[::-1]
