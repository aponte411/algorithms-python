import pytest
from typing import List


def longest_palindromic_subsequence(s: str) -> int:
    def recurse(left: int, right: int, memo: List[List[int]]) -> int:
        if left > right:
            return 0
        if left == right:
            return 1

        if memo[left][right] != -1:
            return memo[left][right]

        if s[left]==s[right]:
            # with both
            return recurse(left+1, right-1, memo) + 2
        else:
            with_left = recurse(left+1, right, memo)
            with_right = recurse(left, right-1, memo)
            memo[left][right] =  max(with_left, with_right)
            return memo[left][right]

    memo = [[-1 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
    return recurse(left=0, right=len(s)-1, memo=memo)

def longest_palindrome_iterative(s: str) -> str:
    """
    Time: O(n^2) worst case, O(n) best case
    Space: O(1)
    """
    if len(s) <= 1:
        return s
    result = ""
    for idx in range(len(s)):
        # odds: center is idx
        left = right = idx
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # update the largest string
            if right - left + 1 > len(result):
                result = s[left:right+1]
            left -= 1
            right += 1
        # evens
        left, right = idx, idx+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(result):
                result = s[left:right+1]
            left -= 1
            right += 1
    return result

@pytest.mark.parametrize(
    "input, expected",
    [("babad", "bab"), ("cbbd", "bb"), ("a", "a")]
)
def test1(input, expected):
    result = longest_palindrome_iterative(s=input)
    assert result == expected

@pytest.mark.parametrize(
    "input, expected",
    [("bbbab", 4), ("cbbd", 2),]
)
def test2(input, expected):
    result = longest_palindromic_subsequence(s=input)
    assert result == expected

pytest.main()

