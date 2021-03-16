import pytest
from typing import List

def get_majority_element(nums: List[int]) -> int:
    """Use baye-moores algorithm"""
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count += 1
        else:
            count -= 1
    return candidate

@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([3,2,3], 3),
        ([2,2,1,1,1,2,2], 2)
    ]
)
def test(inputs, expected):
    result = get_majority_element(inputs)
    assert result == expected

pytest.main()
