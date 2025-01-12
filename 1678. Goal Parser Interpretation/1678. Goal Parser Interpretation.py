"""
Answer to: https://leetcode.com/problems/goal-parser-interpretation/
"""


def solution_1(command: str) -> str:
    """
    This is the optimal solution to the problem.
    The time complexity of this solution is O(n) where n is the length of the command.
    This is because of the for loop that iterates over the command.
    The space complexity of this solution is O(n) where n is the length of the command,
    as a new string is created to store the interpreted command.
    As usual, if the output is not considered the space complexity can be said to be O(1).

    Args:
        command (str): A string representing the command.

    Returns:
        str: The interpreted command.
    """
    ans = ""
    for i, char in enumerate(command):
        if char == "G":
            ans += "G"
        elif char == ")":
            ans += "o" if command[i - 1] == "(" else "al"
    return ans


def solution_2(command: str) -> str:
    """
    This is the optimal solution to the problem.
    The time complexity of this solution is O(n) where n is the length of the command.
    This is because of the replace method that iterates over the command.
    The space complexity of this solution is O(n) where n is the length of the command,
    as a new string is created to store the interpreted command.
    As usual, if the output is not considered the space complexity can be said to be O(1).
    This is the regular expression solution to the problem. It operated in much the
    same way as solution_1 but uses the replace method to replace the substrings instead
    of manually creating a new string.

    Args:
        command (str): A string representing the command.

    Returns:
        str: The interpreted command.
    """
    return command.replace("()", "o").replace("(al)", "al")
