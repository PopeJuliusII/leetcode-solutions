"""
Answer to: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""
from typing import List


def solution_1(boxes: str) -> List[int]:
    """
    This is the optimal solution to the problem.
    It is O(n) time complexity and O(1) or O(n) space complexity,
    depending on whether the answer list is considered as part of the space complexity.
    This is due to the single loop that iterates through the boxes,
    and the use of only four variables to store the number of ones to the left and right.
    In case this solution is unclear, solution_2 has split the loop into two parts,
    potentially making it easier for the reader to understand.

    Args:
        boxes (str): A string of n characters representing n boxes.

    Returns:
        List[int]: A list of integers representing the minimum number of operations
            to move all balls to each box. The ith integer represents the ith box.
    """
    # This will be the answer list to return.
    answer = [0] * len(boxes)

    # The l_ones stores the number of ones to the left of the current box.
    # The l_prev stores the previous total, as if a prefix array were being generated.
    # The r_ones stores the number of ones to the right of the current box.
    # The r_prev stores the previous total, as if a suffix array were being generated.
    l_ones = l_prev = r_ones = r_prev = 0
    for i, b in enumerate(boxes):
        # Update the index with the number of moves required to move all left balls to the current box.
        answer[i] += l_prev + l_ones
        l_prev += l_ones
        l_ones += int(b)

        # Update the index with the number of moves required to move all right balls to the current box.
        answer[~i] += r_prev + r_ones
        r_prev += r_ones
        r_ones += int(boxes[~i])

    return answer


def solution_2(boxes: str) -> List[int]:
    """
    This is a time-optimized solution to the problem.
    It is virtually identical to solution_1, but the loop has been split into two parts
    to make it easier to understand. This solution is O(n) time complexity and O(1) space complexity.
    See solution_1 for a more detailed explanation.

    Args:
        boxes (str): A string of n characters representing n boxes.

    Returns:
        List[int]: A list of integers representing the minimum number of operations
            to move all balls to each box. The ith integer represents the ith box.
    """
    # Initialize an answer list and a variable to store the number of ones.
    # At first, this acts as a prefix array, i.e. the number of ones to the left
    # of the current box is stored in the answer list at each index.
    answer, ones = [], 0
    for b in boxes:
        # The reason for this calculation is because every one to the left of
        # the current box now needs an additional operation to move to the current box.
        answer.append((answer[-1] if answer else 0) + ones)
        ones += int(b)

    # Next, the number of ones to the right of the current box is added to the
    # answer list at each index. This is done by iterating through the boxes in reverse.
    # An even simpler option is to use separate prefix and suffix arrays and combine them,
    # but this uses additional space.
    # Instead, the prev variable is used to isolate what would have been the previous
    # value in a suffix array.
    prev = ones = 0
    for i, b in enumerate(reversed(boxes)):
        # The reason for this calculation is because every one to the right of
        # the current box now needs an additional operation to move to the current box.
        answer[~i] += prev + ones
        prev += ones
        ones += int(b)
    return answer
