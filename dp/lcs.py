import pytest
import functools


"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

a b c d e

a c e

import functools


@functools.lru_cache(None)
def func():
    pass


"""



def lcs(text1: str, text2: str) -> int:

    def helper(p1: int, p2: int) -> int:
        if p1 == M or p2 == N:
            # LCS is 0
            return 0

        if memo[p2][p1] != -1:
            return memo[p2][p1]

        # if they are a match increment both
        if text1[p1] == text2[p2]:
            return helper(p1+1,p2+1) + 1
        # LCS with p1, not p2
        with_curr = helper(p1+1,p2)
        # LCS with p2 not p1
        wo_curr = helper(p1,p2+1)
        # Return the maximum of both results
        memo[p2][p1] =  max(with_curr, wo_curr)
        return memo[p2][p1]

    M, N = len(text1), len(text2)
    memo = [[-1 for _ in range(M+1)] for _ in range(N+1)]

    return helper(p1=0,p2=0)


def lcs2(text1: str, text2: str) -> int:

    @functools.lru_cache(None)
    def recursive(p1: int, p2: int) -> int:
        if p1 == M or p2 == N:
            # LCS is 0
            return 0

        # if they are a match increment both
        if text1[p1] == text2[p2]:
            return recursive(p1+1,p2+1) + 1
        # LCS with p1, not p2
        with_curr = recursive(p1+1,p2)
        # LCS with p2 not p1
        wo_curr = recursive(p1,p2+1)
        # Return the maximum of both results
        return max(with_curr, wo_curr)

    M, N = len(text1), len(text2)

    return recursive(p1=0,p2=0)


def lcs_dp(text1: str, text2: str) -> int:
    M, N = len(text1), len(text2)
    memo = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for i in range(1, M+1):
        for j in range(1, N+1):
            if text1[i-1] == text2[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i][j-1], memo[i-1][j])

    return memo[M][N]


@pytest.mark.parametrize(
    "inputs, expected", [
        (["abcde","ace"], 3),
        (["abc", "def"], 0),
    ]
)
def test_1(inputs, expected):
    result = lcs_dp(inputs[0],inputs[1])
    assert result == expected


pytest.main()
