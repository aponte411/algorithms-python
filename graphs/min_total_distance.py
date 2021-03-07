from collections import namedtuple
from typing import List

Point = namedtuple('Point', ('row', 'col'))

def get_points(grid: List[List[int]]) -> List[Point]:
    points = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # We found someones home
            if grid[row][col] == 1:
                points.append(Point(row, col))
    return points


def calculate_manhattan_distance(
    points: List[Point],
    row: int,
    col: int,
) -> int:
    distance = 0
    for point in points:
        # distance(p1,p2)=|p2.x-p1.x|+|p2.y-p1.y|
        distance += abs(point.row - row) + abs(point.col - col)
    return distance


def min_total_distance(grid: List[List[int]]) -> int:
    points = get_points(grid)
    # if you use float('-inf') you get funny errors
    min_distance = float('inf') # + infinity upper bound
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            distance = calculate_manhattan_distance(
                points,
                row,
                col,
            )
            min_distance = min(min_distance, distance)
    return min_distance

def test():
    grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    expected = 6
    result = min_total_distance(grid)
    print(result)

if __name__ == "__main__":
    test()
