"""
Answer to: https://leetcode.com/problems/defanging-an-ip-address/
"""


def solution_1(address: str) -> str:
    """
    This is the optimal solution to the problem.
    Both time complexity and space complexity are O(n), where n is the length of the address.
    If the return value is not included, the space complexity is O(1).
    The time complexity is due to the list comprehension.

    Args:
        address (str): The IP address.

    Returns:
        str: The defanged IP address.
    """
    return "".join(["[.]" if char == "." else char for char in address])


def solution_2(address: str) -> str:
    """
    This is the optimal solution to the problem.
    Both time complexity and space complexity are O(n), where n is the length of the address.
    If the return value is not included, the space complexity is O(1).
    The time complexity is due to the replace method.

    Args:
        address (str): The IP address.

    Returns:
        str: The defanged IP address.
    """
    return address.replace(".", "[.]")
