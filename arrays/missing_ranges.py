import pytest
from typing import List

def format_range(a: int, b: int) -> str:
    if a == b:
        return str(a)
    return f"{a}->{b}"

def find_missing_ranges(nums: List[int], lower: int, upper: int) -> List[str]:
    if not nums or len(nums) == 0:
        return format_range(lower, upper)

    ranges = []
    # is the first element larger than our lower bound?
    if nums[0] > lower:
        # Add range between first element and lower
        ranges.append(format_range(lower, nums[0] - 1))
    # go through every other number and check adjacent elements
    for i in range(1, len(nums)):
        # Difference greater than 2
        if nums[i] != nums[i-1] and nums[i] > nums[i-1] + 1:
            ranges.append(format_range(nums[i-1]+1, nums[i]-1))
    # last element
    if nums[len(nums)-1] < upper:
        ranges.append(format_range(nums[len(nums)-1]+1, upper))

    return ranges


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([[0,1,3,50,75], 0, 99], ["2","4->49","51->74","76->99"]),
        ([[], 1, 1], "1")
    ]
)
def test_missing_ranges(inputs, expected):
    result = find_missing_ranges(nums=inputs[0], lower=inputs[1], upper=inputs[2])
    assert result == expected

pytest.main()
