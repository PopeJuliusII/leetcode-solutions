"""
Answer to: https://leetcode.com/problems/baseball-game/

Note that the test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
"""
from typing import List


def solution_1(operations: List[str]) -> int:
    """
    This is the optimal solution to the problem.
    The time complexity and space complexity are both O(n)
    where n is the length of the operations list.
    This is because of the for loop iterating over the operations list, and the
    stack storing the points scored during the baseball game.

    Args:
        operations (List[int]): A list of operations to perform during the baseball game.

    Returns:
        int: The sum of the points scored in the baseball game.
    """
    stack = []
    for operation in operations:
        if operation == "+":
            stack.append(stack[-1] + stack[-2])
        elif operation == "D":
            stack.append(stack[-1] * 2)
        elif operation == "C":
            stack.pop()
        else:
            stack.append(int(operation))
    return sum(stack)
