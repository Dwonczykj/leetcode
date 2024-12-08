from typing import Optional
from collections import deque
import math

# `queue = deque([root])` is initializing a deque data structure with the root node of a binary
# tree. The deque is a double-ended queue that allows for efficient insertion and deletion
# operations at both ends. In this case, the root node is added to the deque so that it can be
# used to perform level-order traversal of the binary tree. The deque will be used to keep track
# of the nodes that need to be processed in a specific order during the traversal.
# Definition for a binary tree node.

# BFS: Level-order traversal, uses a queue, explores nodes level by level.
# DFS: Depth-first traversal, uses a stack or recursion, explores nodes branch by branch.

# ### Depth-first traversal
# Depth-First Search (DFS)
# Approach: DFS explores as far down a branch as possible before backtracking. It goes deep into the tree, visiting child nodes before sibling nodes.
# Implementation: DFS can be implemented using a stack, either explicitly with a stack data structure or implicitly with recursion.
# Variants: There are three common types of DFS traversals in binary trees:
# Pre-order: Visit the root, then recursively visit the left subtree, followed by the right subtree.
# In-order: Recursively visit the left subtree, visit the root, and then recursively visit the right subtree. This traversal yields nodes in non-decreasing order for binary search trees.
# Post-order: Recursively visit the left subtree, then the right subtree, and finally visit the root.
# Use Case: DFS is useful when you need to explore all nodes and paths, such as in pathfinding problems or when you need to perform operations on all nodes.

# ### Breadth-first traversal
# Breadth-First Search (BFS)
# Approach: BFS explores all nodes at the present depth level before moving on to nodes at the next depth level. It explores nodes in layers, visiting all nodes at the current depth before moving to the next level.
# Implementation: BFS can be implemented using a queue.
# Use Case: BFS is useful when you need to explore all nodes at the current depth level before moving on, such as in finding the shortest path in an unweighted graph or in tree traversal problems where you need to explore all nodes at the current depth before moving to the next level.
# Example: In a binary tree, BFS would visit nodes in the following order: root, left child of root, right child of root, left child of left child, right child of left child, and so on.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right
        self.depth: Optional[int] = None
        self.parent: Optional[TreeNode] = None

    @property
    def depth_implicit(self):
        if self.parent:
            return self.parent.depth_implicit + 1
        else:
            return 1

    def __str__(self) -> str:
        return f'{self.val}'

    def __repr__(self) -> str:
        return f'[{self.val};d={self.depth}]'

    def __eq__(self, other: object) -> bool:
        return isinstance(other, TreeNode) and self.val == other.val and self.left == other.left and self.right == other.right

    # def __eq__(self, value: object) -> bool:
    #     return isinstance(value, TreeNode) and self.val == value.val

    def init_from_list(cls, values):
        if not values:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            current = queue.popleft()

            if index < len(values) and values[index] is not None:
                current.left = TreeNode(values[index])
                current.left.parent = current
                queue.append(current.left)
            index += 1

            if index < len(values) and values[index] is not None:
                current.right = TreeNode(values[index])
                current.right.parent = current
                queue.append(current.right)
            index += 1

        return root

    def to_list(self) -> list[int | None]:
        """Converts tree to list representation by first appending root and then RECURSIVELY calling to_list on left then right nodes."""
        return [self.val] + (self.left.to_list() if self.left else [None]) + (self.right.to_list() if self.right else [None])

    def print_tree(self):
        root = self
        if not root:
            return

        def height(node: Optional[TreeNode]):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right)) if node else -1

        def fill(res, node, i, l, r):
            if not node:
                return
            mid = (l + r) // 2
            res[i][mid] = str(node.val)
            if node.left:
                res[i + 1][mid - (mid - l) // 2] = '/'
            if node.right:
                res[i + 1][mid + (r - mid) // 2] = '\\'
            fill(res, node.left, i + 2, l, mid - 1)
            fill(res, node.right, i + 2, mid + 1, r)

        h = height(root)
        width = (2 ** (h + 1)) - 1
        res = [[" " for _ in range(width)] for _ in range(2 * h + 1)]
        fill(res, root, 0, 0, width - 1)
        for line in res:
            print("".join(line))


# Example usage
if __name__ == "__main__":
    # Create a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Print the tree
    root.print_tree()
