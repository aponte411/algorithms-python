from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth(root: TreeNode) -> int:
    if not root:
        return 0
    left = depth(root.left)
    right = depth(root.right)
    return max(left, right) + 1


def deepest_leaves_sum(root: TreeNode) -> int:
    # Get max depth
    max_depth = depth(root)
    # Do a BFS and sum the node values at the max depth
    leave_sums = 0
    queue = deque([(root,1)])
    while queue:
        for _ in range(len(queue)):
            node, level = queue.popleft()
            if level == max_depth:
                leave_sums += node.val
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
    return leave_sums


