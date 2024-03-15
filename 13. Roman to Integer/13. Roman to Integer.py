"""
Answer to: https://leetcode.com/problems/roman-to-integer/
"""


def solution_1(s: str) -> int:
    """
    This is the optimal solution to the problem.
    It has a time complexity of O(n) where n is the length of the string.
    It has a space complexity of O(1).
    This is due to the for loop and the use of a dictionary
    to store the values of the Roman numerals. The dictionary's
    size, of course, is constant.

    Args:
        s (str): A string representing a Roman numeral.

    Returns:
        int: The integer value of the Roman numeral.
    """
    conv_dict: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    ans = 0
    for i, char in enumerate(s):
        # Subtract the value of the current character if it is less than the next character.
        if i < len(s) and conv_dict[char] < conv_dict[s[i + 1]]:
            ans -= conv_dict[char]
        # Otherwise, add the value of the current character.
        else:
            ans += conv_dict[char]
    return ans
