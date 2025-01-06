"""
Answer to: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""
from typing import List


def solution_1(boxes: str) -> List[int]:
    """
    This is a time-optimized solution to the problem.
    It is O(n) time complexity and O(n) space complexity,

    Args:
        boxes (str): A string of n characters representing n boxes.

    Returns:
        List[int]: A list of integers representing the minimum number of operations
            to move all balls to each box. The ith integer represents the ith box.
    """
    answer, ones = [], 0
    for b in boxes:
        answer.append((answer[-1] if answer else 0) + ones)
        ones += int(b)
    prev = ones = 0
    for i, b in enumerate(reversed(boxes)):
        answer[~i] += prev + ones
        prev += ones
        ones += int(b)
    return answer
