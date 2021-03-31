import pytest
from collections import deque
from typing import List

def minimum_semesters(n: int, relations: List[List[int]]) -> int:
    graph = {k: [] for k in range(1, n+1)}
    in_degrees = {k: 0 for k in range(1, n+1)}
    for edge in relations:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degrees[child] += 1

    sources = deque([])
    for node in in_degrees:
        if in_degrees[node] == 0:
            sources.append((node, 1))

    semesters = 0
    visited = set()
    while sources:
        node, level = sources.popleft()
        visited.add(node)
        # max levels to complete all courses
        semesters = max(semesters, level)
        for child in graph[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append((child, level+1))
    return semesters if len(visited) == n else -1


def test():
    n = 3
    relations = [[1, 3],[2,3]]
    expected = 2
    result = minimum_semesters(n, relations)
    assert result == expected

pytest.main()
