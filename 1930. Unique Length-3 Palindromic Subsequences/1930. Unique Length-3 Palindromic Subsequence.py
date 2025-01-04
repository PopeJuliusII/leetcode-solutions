"""
Answer to: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
"""


def solution_1(s: str) -> int:
    """
    This is a time-optimized solution to the problem.
    It is O(n) time complexity and O(1) space complexity.
    This is due to the use of a single for loop to iterate through
    the string for preprocessing. The dictionary can have at most
    26 entries, one for each lowercase English letter, making the
    space complexity O(1). Additional markers for time and space
    complexity are included in the comments.

    Args:
        s (str): A string of lowercase English letters.

    Returns:
        int: The number of unique length-3 palindromic subsequences.
    """
    # The format will be k: [first_index, last_index].
    # SPACE: O(1) because there are at most 26 entries.
    instances = {}
    # TIME: O(n) where n is the length of s.
    for i, char in enumerate(s):
        if char not in instances:
            instances[char] = [i, i]
        else:
            instances[char][-1] = i

    # The sum of the length of the unique characters between the first and last index.
    # This could also be written as:
    # return sum(len(set(s[start + 1 : end])) for (start, end) in instances.values() if start != end)
    # but the code below does not create a new string for each instance.
    cnt = 0
    # TIME: O(1) because there are at most 26 entries.
    for start, end in instances.values():
        if start != end:
            char_set = set()
            # TIME: O(n) where n is the length of the substring.
            for i in range(start + 1, end):
                char_set.add(s[i])
            cnt += len(char_set)
    return cnt
