import pytest
from typing import List

def rotate_90_degrees(matrix: List[List[int]]):
    """rotate the corners: topleft->bottom-left->bottom-right
    ->top-right"""
    left, right = 0, len(matrix)-1
    while left < right:
        # setup square: L, R, top, bottom
        top, bottom = left, right
        # Go through every cell
        for cell in range(right - left):
            # save topLeft to orient swaps
            topLeft = matrix[top][left+cell]
            # begin swaps: move bottom left to top left
            matrix[top][left+cell] = matrix[bottom-cell][left]
            # move bottom right into bottom left
            matrix[bottom-cell][left] = matrix[bottom][right-cell]
            # move top right into bottom right
            matrix[bottom][right-cell] = matrix[top+cell][right]
            # move top left into top right
            matrix[top+cell][right] = topLeft

        # rotate
        left += 1
        right -= 1

def test():
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    rotate_90_degrees(matrix)
    assert matrix == expected

