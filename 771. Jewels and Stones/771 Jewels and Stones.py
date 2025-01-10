"""
Answer to: https://leetcode.com/problems/jewels-and-stones/
"""


def solution_1(jewels: str, stones: str) -> int:
    """
    This is the time optimal solution to the problem.
    The time complexity of this solution is O(n + m) where n is the length of jewels and m is the length of stones.
    This is because of the set creation and the iteration over the list of stones.
    The space complexity of this solution is O(n) where n is the length of jewels because of the set creation.

    Args:
        jewels (str): A string of distinct characters representing the types of stones that are jewels.
        stones (str): A string of characters representing the stones one has.

    Returns:
        int: The number of stones that are jewels.
    """
    jewels_set = set(jewels)
    return sum(stone in jewels_set for stone in stones)


def solution_2(jewels: str, stones: str) -> int:
    """
    This is the space optimal solution to the problem.
    The time complexity of this solution is O(n * m) where n is the length of jewels and m is the length of stones.
    This is because of the nested for loop iterating over the list of jewels and stones.
    The space complexity of this solution is O(1) because we are not using any extra space.

    Args:
        jewels (str): A string of distinct characters representing the types of stones that are jewels.
        stones (str): A string of characters representing the stones one has.

    Returns:
        int: The number of stones that are jewels.
    """
    return sum(stone in jewels for stone in stones)
