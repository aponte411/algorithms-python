from typing import List

class GraphNode:
    WHITE, GRAY, BLACK = range(3)
    def __init__(self) -> None:
        self.color = GraphNode.WHITE
        self.edges: List['GraphNode'] = []

# O(Nodes + Edges) time and O(Nodes) space
def is_deadlocked(graph: List[GraphNode]) -> bool:
    def has_cycle(node: GraphNode) -> bool:
        # If weve already starting processing this node, that means weve already
        # seen it - therefore we have a cycle in the graph. Another way to look at this
        # is if we encounter a "back edge" - a edge from a descendent to an ancestor node
        if node.color == GraphNode.GRAY:
            return True
        # start exploration
        node.color = GraphNode.GRAY
        # search through neighbors
        for neighbor_node in node.edges:
            # If were still searching (WHITE, GRAY) and theres a cycle, report
            if neighbor_node.color != GraphNode.BLACK and has_cycle(neighbor_node):
                return True
        # finish exploration
        node.color = GraphNode.BLACK
        return False

    # Go through graph and check for dealocks: we see a neighbor node with a GRAY state
    for node in graph:
        if node.color == GraphNode.WHITE and has_cycle(node):
            return True
    # Else no, deadlock
    return False

