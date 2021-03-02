from collections import deque
"""
Use BFS to iterate through the graph and enqueue any new node that we havent seen before using a
dictionary that maps original nodes to their cloned counterparts. We can clone a node by instantiating
a new GraphNode instance and setting the node we are currently processing (e.g. GRAY if were using WHITE, GRAY, BLACK) label
to cloned counterpart.
"""

class GraphNode:
    def __init__(self, label: int) -> None:
        self.label = label
        self.edges: List['GraphNode'] = []

# O(Nodes + Edges) time, O(Nodes) space
def clone_graph(graph: GraphNode) -> GraphNode:
    if not graph:
        return
    # BFS with a queue
    q = deque([graph])
    # Store map of original to clone nodes
    node_map = {graph: GraphNode(graph.label)}
    # Start from u and everytime we encounter a new node, clone it
    while q:
        node = q.popleft()
        for neighbor in node.edges:
            # Clone neighbor
            if neighbor not in node_map:
                # Store original as key and clone as value
                node_map[neighbor] = GraphNode(neighbor.label)
                q.append(neighbor)
            # Store original 'parent' node as key and add neighbor edges
            node_map[node].edges.append(node_map[neighbor])

    return node_map
