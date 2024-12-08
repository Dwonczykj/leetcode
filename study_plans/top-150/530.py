# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from typing import Optional

from binary_tree_node import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        if root and not root.left and not root.right:
            return -1

        q = deque([root])
        l: list[int] = [root.val]
        while q:
            node = q.pop()
            if node.left:
                q.append(node.left)
                l.append(node.left.val)
            if node.right:
                q.append(node.right)
                l.append(node.right.val)
            # do any specific function logic
        l.sort()
        min_diff = float("inf")
        for i in range(1, len(l)):
            if l[i] - l[i-1] < min_diff:
                min_diff = l[i] - l[i-1]
            if min_diff == 0:
                return min_diff
        return min_diff


def tn(nums: list[int | None]):
    return TreeNode.init_from_list(TreeNode, nums)


if __name__ == "__main__":
    sol = Solution()
    null = None
    kwargs_list = [
        ({"root": [3, 9, 20, None, None, 15, 7], }, 2),
        ({"root": [1, None, 2], }, 1),
        ({"root": [1, None, 3, None, 3], }, 0),
        ({"root": [1, None, 1], }, 0),
        ({"root": [], }, -1),
        ({"root": [2], }, -1),
        ({"root": [2, None, 1, 5, 3], }, 1),
        ({"root": [2, None, 1, 5, 3, None, 4, 8, None], }, 1),
        ({"root": [1, 2, 5, 3, 4, None, 6], }, 1),
    ]
    for kwargs, expected in kwargs_list:
        print("-"*30+f"\nNew Solution: {kwargs}")
        root = tn(kwargs["root"])
        result = sol.getMinimumDifference(root=root)
        assert result == expected
