"""
Answer to: https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/
"""


def solution_1(s: str) -> int:
    """
    This is the easiest solution to understand.

    Args:
        s (str): A string of digits.

    Returns:
        int: The number of unique substrings with equal digit frequency.
    """
    seen = set()
    for start, _ in enumerate(s):
        cnt = {}
        for end in range(start, len(s)):
            cnt[s[end]] = cnt.get(s[end], 0) + 1
            if len(set(cnt.values())) == 1:
                seen.add(s[start : end + 1])
    return len(seen)
