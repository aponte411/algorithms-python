from collections import namedtuple, deque
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
    """
    Time: O(m^2 * n^2)
    Space: O(m^2, n^2)
    For each node in the grid we calculate the manhattan distance.
    """
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

Node = namedtuple('Node', ('x', 'y', 'dist'))


def min_total_distance_bfs(self, grid: List[List[int]]) -> int:
    def bfs(x: int, y: int) -> int:
        total_distance = 0
        # create set
        visited = [[False]*n for _ in range(m)]
        que = deque([Node(x, y, 0)])
        while que:
            node = que.popleft()
            if not (0 <= node.x < m and 0 <= node.y < n) or visited[node.x][node.y]:
                continue
            # If we find a home
            if grid[node.x][node.y] == 1:
                total_distance += node.dist
            visited[node.x][node.y] = True
            que.append(Node(node.x + 1, node.y, node.dist+1))
            que.append(Node(node.x - 1, node.y, node.dist+1))
            que.append(Node(node.x, node.y+1, node.dist+1))
            que.append(Node(node.x, node.y-1, node.dist+1))

        return total_distance

    m = len(grid)
    n = len(grid[0])
    min_distance = float('inf')
    for row in range(m):
        for col in range(n):
            distance = bfs(row, col)
            min_distance = min(min_distance, distance)
    return min_distance

def test():
    grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
    expected = 6
    result = min_total_distance(grid)
    print(result)
    assert result == expected

if __name__ == "__main__":
    test()
