# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150


from collections import deque
from typing import List, Optional
from binary_tree_node import TreeNode

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q: deque[TreeNode] = deque([root])

        result = []
        while q:
            right_most = None
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                right_most = node.val
            result.append(right_most)
        return result


def tn(nums: list[int | None]):
    return TreeNode.init_from_list(TreeNode, nums)


if __name__ == "__main__":
    sol = Solution()
    null = None
    kwargs_list = [
        ({"root": [1, 2, 3, null, 5, null, 4], }, [1, 3, 4]),
    ]
    for kwargs, expected in kwargs_list:
        print("-"*30+f"\nNew Solution: kwargs = {kwargs}")
        result = sol.rightSideView(root=tn(kwargs["root"]))
        assert result == expected
