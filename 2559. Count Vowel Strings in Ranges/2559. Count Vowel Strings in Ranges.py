"""
Answer to: https://leetcode.com/problems/count-vowel-strings-in-ranges/

Note that the space optimized solution is not included in this file as
the constraints are so large that a nested for loop is not feasible.
Also note that the queries are 0-indexed and inclusive.
"""
from typing import List
from itertools import accumulate


def solution_1(words: List[str], queries: List[List[int]]) -> List[int]:
    """
    This is a time-optimized solution to the problem.
    It is O(m + n) time complexity and O(n) space complexity,
    where m is the number of queries and n is the length of the list of words.
    The space complexity is due to the use of a prefix sum to store the number of
    words that start and end with a vowel up to each index. The time complexity is
    due to iterating over the list of words to create the prefix sum and then
    iterating over the list of queries to calculate the number of words that
    start and end with a vowel in each range.

    Args:
        words (List[str]): A list of words to search.
        queries (List[List[int]]): A list of queries to perform on the words.
            Each query is a list of two integers, inclusive.
            Each element is in the range [0, n - 1], where n is the length of words.

    Returns:
        List[int]: The number of words with the range for each query which both start and end with a vowel.
    """
    # A set of vowels for easier access.
    VOWELS = set("aeiou")

    # Create a prefix sum of the number of words that start and end with a vowel.
    prefix_sum = list(accumulate((w[0] in VOWELS and w[-1] in VOWELS for w in words)))

    # Return the answer, as requested.
    return [prefix_sum[b] - (prefix_sum[a - 1] if a else 0) for a, b in queries]
