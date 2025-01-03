"""
Answer to: https://leetcode.com/problems/number-of-ways-to-split-array/

Note that the split cannot be at the last index, as the split is
considered to be part of the left side and a split at the final
index would result in an empty right side.
"""
from typing import List


def solution_1(nums: List[int]) -> int:
    """
    This is the optimal solution to the problem.
    It is O(n) time complexity and O(1) space complexity,
    where n is the length of nums. This is due to the use of
    sum and a single for loop to iterate through the list.

    Args:
        nums (List[int]): A list of integers to split.

    Returns:
        List[int]: The number of indices at which the array, nums, can be split at.
    """
    cnt, left, right = 0, 0, sum(nums)

    # Range is used because otherwise a check would be needed at every iteration
    # to ensure that the last element is not included. One cannot split the array
    # at the last element.
    for i in range(len(nums) - 1):
        right -= nums[i]
        left += nums[i]
        cnt += right <= left
    return cnt
