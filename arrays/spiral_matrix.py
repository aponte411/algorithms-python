import pytest
from typing import List

def spiral_matrix(matrix: List[List[int]]) -> List[List[int]]:
    result: List[List[int]] = []
    ROWS, COLS = len(matrix), len(matrix[0])
    seen = [[False for _ in range(COLS)] for _ in range(ROWS)]
    diags = ((0, 1),(1,0), (0,-1),(-1,0))
    diag, row, col = 0, 0, 0
    for _ in range(ROWS):
        for _ in range(COLS):
            result.append(matrix[row][col])
            seen[row][col] = True
            new_row, new_col = row + diags[diag][0], col + diags[diag][1]
            # If valid, update row and col
            if (0 <= new_row < ROWS and 0 <= new_col < COLS) and not seen[new_row][new_col]:
                row, col = new_row, new_col
            # Else, update dig by taking the mod
            else:
                diag = (diag + 1)%4
                row, col = row + diags[diag][0], col + diags[diag][1]
    return result


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
    ]
)
def test_spiral_matrix(inputs, expected):
    result = spiral_matrix(matrix=inputs)
    assert result == expected

pytest.main()
