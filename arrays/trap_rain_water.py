import pytest
from typing import List

def compute_trapped_water(heights: List[int]) -> int:
    trapped_water = 0
    # Go left to right and compute and max of left
    # and max of right. Well use that to compute the amount
    # of trapped water.
    left, right = 0, len(heights)-1
    max_left, max_right = 0, 0
    while left < right:
        # compute max left and max right
        max_left = max(max_left, heights[left])
        max_right = max(max_right, heights[right])
        # Use the largest of the two to compute the
        # water level: max - current_height
        if max_right > max_left:
            water_level = max_left - heights[left]
            trapped_water += water_level
            left += 1
        else:
            water_level = max_right - heights[right]
            trapped_water += water_level
            right -= 1

    return trapped_water

@pytest.mark.parametrize(
    "inputs, expected",
    [([0,1,0,2,1,0,1,3,2,1,2,1], 6), ([4,2,0,3,2,5], 9)]
)
def test(inputs, expected):
    result = compute_trapped_water(heights=inputs)
    assert result == expected

pytest.main()


