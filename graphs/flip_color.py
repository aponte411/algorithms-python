from collections import deque
from typing import List

def flip_colors_bfs(x: int, y: int, image: List[List[bool]]) -> None:
    color = image[x][y]
    # initialize queue
    q = deque([x, y])
    # flip color
    image[x][y] = not image[x][y]
    while q:
        x, y = q.popleft()
        # search through image and when we find the same color flip it
        for next_x, next_y in ((x, y+1),(x,y-1),(x+1,y),(x-1,y)):
            # check if out of bounds
            if (0 <= next_x < len(image) and 0 <= next_y < len(image[0])) and \
                    image[next_x][next_y]==color:
                # neighbors colors
                image[next_x][next_y] = not image[next_x][next_y]
                # add neighbor to queue
                q.append((next_x, next_y))

def flip_colors_dfs(x: int, y: int, image: List[List[bool]]) -> None:
    color = image[x][y]
    image[x][y] = not image[x][y]
    for next_x, next_y in ((x, y+1),(x,y-1),(x+1,y),(x-1,y)):
        # check if out of bounds
        if (0 <= next_x < len(image) and 0 <= next_y < len(image[0])) and image[next_x][next_y]==color:
            # neighbors colors
            flip_colors_dfs(next_x, next_y, image)

