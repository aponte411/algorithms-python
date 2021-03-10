import pytest
from typing import List

def longest_increasing_subsequence(nums: List[int]) -> int:
    def helper(index: int, prev: int) -> int:
        if index == len(nums):
            return 0
        with_index = 0
        if nums[index] > prev:
            with_index = 1 + helper(index+1, nums[index])
        without = helper(index+1, prev)
        return max(with_index, without)

    return helper(0, float('-inf'))

def longest_increasing_subsequence_dp(nums: List[int]) -> int:
    N = len(nums)
    table = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i):
            if nums[i] > nums[j]:
                table[i] = max(table[i], table[j] + 1)
    return max(table)




@pytest.mark.parametrize(
    "inputs, expected", [([10,9,2,5,3,7,101,18], 4)]
)
def test1(inputs, expected):
    result = longest_increasing_subsequence(nums=inputs)
    assert result == expected

@pytest.mark.parametrize(
    "inputs, expected", [([10,9,2,5,3,7,101,18], 4)]
)
def test2(inputs, expected):
    result = longest_increasing_subsequence_dp(nums=inputs)
    assert result == expected


pytest.main()
