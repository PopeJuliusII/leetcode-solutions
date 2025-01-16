"""
https://leetcode.com/problems/convert-the-temperature/
"""
from typing import List


def solution_1(celsius: float) -> List[float]:
    """
    This is the optimal solution to the problem.
    Both time complexity and space complexity are O(n).

    Args:
        celsius (float): The temperature in celsius.

    Returns:
        List[int]: The temperature converted into a list of the format [kelvin, fahrenheit].
    """
    return [celsius + 273.15, celsius * 1.8 + 32]
