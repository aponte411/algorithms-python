import pytest
from typing import List

def can_partition_subset(nums: List[int]) -> bool:
    subset_total = sum(nums)
    if subset_total % 2 != 0:
        return False
    target = subset_total//2
    dp = [False for _ in range(target+1)]
    dp[0] = True
    for i in range(len(nums)):
        t = target
        while t >= nums[i]:
            dp[t] = dp[t] or dp[t - nums[i]]
            t -= 1
    return dp[target]

@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([1,5,11,5], True),
        ([1,2,3,5], False)
    ]
)
def test_dp_approach(inputs, expected):
    result = can_partition_subset(nums=inputs)
    assert result == expected

pytest.main()

