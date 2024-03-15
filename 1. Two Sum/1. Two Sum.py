"""
Answer to: https://leetcode.com/problems/two-sum/

Note that the problem statement guarantees that there is always exactly one solution.
"""
from typing import List


def solution_1(nums: List[int], target: int) -> List[int]:
    """
    This is a time-optimized solution to the problem.
    It is O(n) time complexity and O(n) space complexity,
    where n is the length of the list of numbers. This is due
    to the use of a dictionary to store the index of each number
    and the for loop enumerating nums.

    Args:
        nums (List[int]): A list of integers to search.
        target (int): Find two numbers that add up to the target.

    Returns:
        List[int]: The index of the two numbers in the list which add up to the target.
            The problem statement guarantees that there is exactly one solution.
    """
    # Create a dictionary to store the index of each number in the list.
    num_index: dict[int, int] = {}

    # Iterate through the list of numbers.
    for idx, num in enumerate(nums):
        # Check if the complement of the current number is in the dictionary.
        complement: int = target - num

        # If the complement is in the dictionary, return the indices of the two numbers.
        if complement in num_index:
            return [num_index[complement], idx]

        # Set the number to the index in the dictionary.
        num_index[num] = idx


def solution_2(nums: List[int], target: int) -> List[int]:
    """
    This is a space-optimized solution to the problem.
    It is O(n^2) time complexity and O(1) space complexity,
    where n is the length of the list of numbers. This is due
    to the use of two nested for loops to iterate through the list.

    Args:
        nums (List[int]): A list of integers to search.
        target (int): Find two numbers that add up to the target.

    Returns:
        List[int]: The index of the two numbers in the list which add up to the target.
            The problem statement guarantees that there is exactly one solution.
    """
    # Iterate over the list of numbers.
    for i, n1 in enumerate(nums):
        # Iterate over the list of numbers again.
        for j in range(i + 1, len(nums)):
            # Check if the two numbers add up to the target.
            if n1 + nums[j] == target:
                return [i, j]
