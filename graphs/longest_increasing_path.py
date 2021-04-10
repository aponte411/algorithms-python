import pytest
from typing import List


def longest_increasing_path(matrix: List[List[int]]) -> int:
    def backtrack(row: int, col: int) -> int:
        if cache[row][col] != -1:
            return cache[row][col]

        len_of_path = 0
        for new_row, new_col in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                len_of_path = max(len_of_path, backtrack(new_row, new_col))
        cache[row][col] = len_of_path + 1
        return cache[row][col]

    rows = len(matrix)
    cols = len(matrix[0])
    cache = [[-1 for col in range(cols)] for row in range(rows)]

    max_len = 0
    for row in range(rows):
        for col in range(cols):
            max_len = max(max_len, backtrack(row, col))
    return max_len


def test():
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    expected = 4
    result = longest_increasing_path(matrix)
    assert result == expected

pytest.main()
