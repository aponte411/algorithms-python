from collections import namedtuple
from typing import List

# WHITE = unvisited
# BLACK = visited
WHITE, BLACK = 0, 1

Coordinate = namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze: List[List[int]], start: Coordinate, end: Coordinate) -> List[Coordinate]:
    def dfs(coordinate: Coordinate) -> bool:
        # Check that the coordinate isn't about of bounds
        if not (0 <= coordinate.x < len(maze) \
                and 0 <= coordinate.y < len(maze[coordindate.x]) \
                and maze[coordinate.x][coordinate.y] == WHITE:
            return False
        # Add current coordinate
        path.append(coordinate)
        # Star exploration by marking
        maze[coordinate.x][coordinate.y] = BLACK
        if coordinate == end:
            return True
        for x, y in [(coordinate.x - 1, coordinate.y), (coordinate.x + 1, coordinate.y), (coordinate.x, coordinate.y - 1), (coordinate.x, coordinate.y + 1)]:
            if dfs(Coordinate(x, y)):
                return True
        # if we didnt find a path, backtrack
        path.pop()
        return False

    path: List[Coordinate] = []
    dfs(start)
    return path

