"""
Answer to: https: https://leetcode.com/problems/simplify-path/
"""


def solution_1(path: str) -> str:
    """
    This is the optimal solution to the problem.
    It has a time complexity of O(n) and a space complexity of O(n),
    where n is the length of the path. This is due to iterating over
    the path and using a stack to store the directories.

    Args:
        path (str): A string representing a Unix-style path.

    Returns:
        str: The simplified version of the path.
    """
    stack = []
    for part in path.split("/"):
        if part == "..":
            stack and stack.pop()
        elif part != ".":
            part and stack.append(part)
    return "/" + "/".join(stack)
