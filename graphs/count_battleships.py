from typing import List

"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

# In this example there are 2 battleships.
X..X
...X
...X

# Example of invalid board you will never see.
...X
XXXX
...X

X.X.
.X..
X.X.


# board
[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

# DFS - walking through a maze, whenever we hit a walk we just back the
way we came in, and go down another path...and so and so forth.
"""

def dfs(row: int, col: int, board: List[List[str]]):
    rows = len(board)
    cols = len(board[0])
    # If out of bounds or == "." go back
    if not (0 <= row < rows and 0 <= col < cols) or board[row][col] != "X":
        return

     # begin processing
    board[row][col] = "#"
    for next_row, next_col in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
        dfs(next_row, next_col, board)
    # End of processing



def count_battleships(board: List[List[str]]) -> int:
    count = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "X":

                dfs(row, col, board)
                count += 1

    return count


def test():
    board = [
        ["X",".",".","X"],
        [".",".",".","X"],
        [".",".",".","X"],
    ]
    expected = 2
    result = count_battleships(board=board)
    assert result == expected
    print("Test passed!")

if __name__ == "__main__":
    test()
