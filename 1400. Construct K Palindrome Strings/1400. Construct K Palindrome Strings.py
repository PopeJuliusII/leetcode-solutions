"""
Answer to: https://leetcode.com/problems/construct-k-palindrome-strings/
"""


def solution_1(s: str, k: int) -> bool:
    """
    This is the optimal solution to the problem.


    Args:
        s (str): A string of lowercase English letters.
        k (int): An integer representing the number of palindromic strings one should aim to construct.

    Returns:
        bool: A boolean value indicating whether it is possible to construct k palindromic strings from s.
    """
    # len(s) is the maximum number of palindromic strings that can be constructed.
    # The check is done here to avoid unnecessary computation if the request is facially impossible.
    if len(s) < k:
        return False

    # This will count the number of characters that have an odd frequency.
    # Add and remove characters from the set whilst iterating over the string.
    char_set = set()
    for char in s:
        if char in char_set:
            char_set.discard(char)
        else:
            char_set.add(char)

    # The number of characters with an odd frequency is the minimum number of palindromic strings that can be constructed.
    # The number of palindromes required should be more than or equal to the minimum number of palindromes that can be constructed.
    return len(char_set) <= k
