"""
Answer to: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
"""


def solution_1(s: str) -> int:
    """
    This is the optimal solution to the problem.

    Args:
        s (str): A string to split.

    Returns:
        int: The maximum score after splitting the string.
    """
    # The key to this approach is fairly straightforward. One must maximize:
    # left_zeroes + total_ones - left_ones
    # As total_ones is a constant, the aim becomes to maximize left_zeroes - left_ones.
    # max_val stores the maximum value of left_zeroes - left_ones.
    max_val, zeroes, ones = -1, 0, 0
    for i, char in enumerate(s):
        # Increment the correct counter.
        if char == "1":
            ones += 1
        else:
            zeroes += 1

        # Maximize left_zeroes - left_ones.
        if i != len(s) - 1:
            max_val = max(max_val, zeroes - ones)

    # Return the maximum score, i.e. total_ones + left_zeroes - left_ones.
    return ones + max_val
