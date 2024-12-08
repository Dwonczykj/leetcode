# 114. Flatten Binary Tree to Linked List
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from typing import Optional
from binary_tree_node import TreeNode
from test_helper import tn

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


class Solution:
    def __init__(self) -> None:
        self.prev: Optional[TreeNode] = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # self.flatten_recursion(root)
        self.flatten_iterative(root)

    def flatten_recursion(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        # It helps to think about how this fucntino approaches the leaves first as it is recursive and then work backwards.

        # Process right subtree first
        self.flatten_recursion(root.right)

        # Process left subtree
        self.flatten_recursion(root.left)

        # Set the current node's right to prev and left to null
        root.right = self.prev  # top of the root.left unless this was None in which case that call returned before setting prev and therefore will be root.right, unless again root.right is None in which chase prev is this which again is None at the root of the tree.
        root.left = None

        # Update prev to current node
        self.prev = root

    def flatten_iterative(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = deque([root])

        while stack:
            current = stack.pop()

            # Push right and then left child to the stack
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            # Modify the current node's right to point to the next node in the stack
            if stack:
                current.right = stack[-1]

            # Set the left to null
            current.left = None

    def run(self, root: Optional[list[int | None]]):
        treeNode = tn(nums=root) if root else None
        return self.flatten(root=treeNode)


if __name__ == "__main__":
    sol = Solution()
    null = None
    kwargs_list = [
        # ({"root": [3, 9, 20, None, None, 15, 7], }, 3),
        # ({"root": [1, None, 2], }, 2),
        # ({"root": [], }, 0),
        # ({"root": [2], }, 1),
        # ({"root": [2, None, 1, 5, 3], }, 3),
        # ({"root": [2, None, 1, 5, 3, None, 4, 8, None], }, 4),
        ({"root": [1, 2, 5, 3, 4, None, 6], }, [
         1, None, 2, None, 3, None, 4, None, 5, None, 6, None, None]),
    ]
    for kwargs, expected in kwargs_list:
        print("-"*30+f"\nNew Solution: {kwargs}")
        result = tn(kwargs["root"])
        sol.flatten(root=result)
        y = result.to_list()
        assert y == expected
