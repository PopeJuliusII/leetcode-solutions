"""
Answer to: https://leetcode.com/problems/number-of-employees-who-met-the-target/
"""
from typing import List


def solution_1(hours: List[int], target: int) -> int:
    """
    This is the optimal solution to the problem.
    The time complexity of this solution is O(n) where n is the number of employees.
    This is because of the iteration over the list of hours.
    The space complexity of this solution is O(1) because we are not using any extra space.

    Args:
        hours (List[int]): A list of integers representing the hours worked by each employee.
        target (int): The target number of hours that an employee must work to be considered as meeting the target.

    Returns:
        int: The number of employees who met the target.
    """
    return sum(h >= target for h in hours)
