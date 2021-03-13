import pytest
from collections import defaultdict


def min_steps(s: str, t: str) -> int:
    # count the number of chars of s
    # and then walk through t, if we have seen that
    # number before decrement it,
    # else increment the 'steps' pointer
    # which holds the number of steps we'd need to
    # take a step to make it an anagram
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1

    steps = 0
    for char in  t:
        if counts[char]:
            counts[char] -= 1
        else:
            steps += 1
    return steps

@pytest.mark.parametrize(
    "input, expected",
    [(["bab","aba"],1),(["leetcode","practice"],5)]
)
def test(input, expected):
    result = min_steps(input[0], input[1])
    assert result == expected

pytest.main()
