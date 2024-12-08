#  104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional
from binary_tree_node import TreeNode


def tn(nums: list[int | None]):
    return TreeNode.init_from_list(TreeNode, nums)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        q: deque[TreeNode] = deque()
        if root:
            root.print_tree()
            q.append(root)
        while q:
            depth += 1
            # the next 2 lines are key to only pop the nodes from previous iteration
            # so that we come out of the for loop for the next level to increment depth above.
            print(f"reached depth: [{depth}] with queue: {q}")
            for _ in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return depth

    def run(self, root: Optional[list[int | None]]):
        treeNode = tn(nums=root) if root else None
        return self.maxDepth(root=treeNode)


if __name__ == "__main__":
    sol = Solution()
    null = None
    kwargs_list = [
        # ({"root": [3, 9, 20, None, None, 15, 7], }, 3),
        # ({"root": [1, None, 2], }, 2),
        # ({"root": [], }, 0),
        # ({"root": [2], }, 1),
        # ({"root": [2, None, 1, 5, 3], }, 3),
        ({"root": [2, None, 1, 5, 3, None, 4, 8, None], }, 4),
    ]
    for kwargs, expected in kwargs_list:
        print("-"*30+f"\nNew Solution: {kwargs}")
        result = sol.run(**kwargs)
        # x = tn(expected)
        assert result == expected
