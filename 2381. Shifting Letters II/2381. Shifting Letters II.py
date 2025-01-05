"""
Answer to: https://leetcode.com/problems/shifting-letters-ii/
"""
from typing import List


def solution_1(s: str, shifts: List[List[int]]) -> str:
    """
    This is the optimal solution to the problem.
    The time complexity is O(m + n), where m is the length of shifts
    and n is the length of s. This is because of the iteration over shifts and
    two iterations over s, hence O(m + n). The space complexity is O(n), where n,
    again, is the length of s. This is due to the creation of the prefix sum list.
    Note that technically, this is the time-optimized solution, as the space complexity
    could be reduced to O(1) by modifying the string as one iterates over the shift.
    However, this would make the time complexity so great as to render the solution
    unfeasible. Therefore, this is the optimal solution.

    Args:
        s (str): A string to shift.
        shifts (List[List[int]]): A list of shifts to apply to the string.
            Of the format [start, end, shift], 0-indexed and inclusive.
            If shift is 1, the character at index i will be shifted up, i.e. a -> b, z -> a, etc.
            If shift is 0, the character at index i will be shifted down, i.e. b -> a, a -> z, etc.

    Returns:
        str: The string after applying the shifts.
    """
    # This will create a prefix sum list of the shifts.
    # In essence, it will keep track of the total shift at each index as one progresses
    # through the string.
    prefix_sum = [0] * len(s)
    for start, end, change in shifts:
        prefix_sum[start] += change or -1

        # This is to ensure that the end index is not out of bounds, as shifts is inclusive.
        if end < len(s) - 1:
            prefix_sum[end + 1] -= change or -1

    # This creates a prefix sum list of the shifts.
    # [0, 1, -2] means that the first character should be shifted 0 times, the second
    # character should be shifted 1 time, and the third character should be shifted -2 times, i.e.
    # shifted down 2 times.
    for i in range(1, len(s)):
        prefix_sum[i] += prefix_sum[i - 1]

    # This will shift the characters in the string according to the prefix sum list.
    return "".join(
        chr((ord(char) - 97 + prefix_sum[i]) % 26 + 97) for i, char in enumerate(s)
    )
