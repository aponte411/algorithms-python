from dataclasses import dataclass
from typing import List

@dataclass
class GraphNode:
    edges: List['GraphNode'] = []
    max_distance: int = 0

def find_largest_number_of_teams(graph: List['GraphNode']) -> int:
    def dfs(node: 'GraphNode'):
        if not node:
            return
        neighbor_distances = []
        for neighbor in node.edges:
            if neighbor.max_distance != 0:
                neighbor_distances.append(neighbor.max_distance)
            else:
                neighbor_distance = dfs(neighbor) + 1
                neighbor_distances.append(neighbor_distance)
        return max(neighbor_distances)

    distances = []
    for node in graph:
        if node.max_distance == 0:
            distances.append(dfs(node))
    return max(distances)

