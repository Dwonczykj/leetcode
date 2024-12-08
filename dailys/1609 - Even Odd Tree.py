from collections import deque, defaultdict
from typing import List, Optional, Tuple, Set
from objects.binary_tree_node import TreeNode

import random
import math

'''
# [1609. Even Odd Tree](https://leetcode.com/problems/even-odd-tree/description/?envType=daily-question&envId=2024-07-21)

A binary tree is named **Even-Odd**  if it meets the following conditions:

- The root of the binary tree is at level index `0`, its children are at level index `1`, their children are at level index `2`, etc.
- For every **even-indexed**  level, all nodes at the level have **odd**  integer values in **strictly increasing**  order (from left to right).
- For every <b>odd-indexed</b> level, all nodes at the level have <b>even</b> integer values in **strictly decreasing**  order (from left to right).

Given the `root` of a binary tree, return `true` if the binary tree is **Even-Odd** , otherwise return `false`.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/sample_1_1966.png" style="width: 362px; height: 229px;">

```
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
Explanation: The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/sample_2_1966.png" style="width: 363px; height: 167px;">

```
Input: root = [5,4,2,3,3,7]
Output: false
Explanation: The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.
```

**Example 3:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/22/sample_1_333_1966.png" style="width: 363px; height: 167px;">

```
Input: root = [5,9,1,3,5,7]
Output: false
Explanation: Node values in the level 1 should be even integers.
```

**Constraints:** 

- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^6`
'''

# Definition for a binary tree node. - Moved to own file
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        isEvenOddTree = True
        level = 0
        while q:
            next_children = []
            evenIndLvl = level % 2
            prev_n = None
            for i in range(len(q)):
                n = q[i]
                if not n:
                    continue
                isEvenOddTree = n.val % 2 == (
                    0 if evenIndLvl == 1 else 1)
                if not isEvenOddTree:
                    return False
                next_children.append(n.left)
                next_children.append(n.right)
                if prev_n:
                    if evenIndLvl == 0:
                        isEvenOddTree = prev_n.val < n.val
                    else:
                        isEvenOddTree = prev_n.val > n.val
                if not isEvenOddTree:
                    return False
                prev_n = n
            q = next_children
            level += 1
        return isEvenOddTree


runner = Solution()
root = TreeNode.init_from_list(
    TreeNode, [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2])
isEven = runner.isEvenOddTree(root)
assert isEven == True

root = TreeNode.init_from_list(TreeNode, [5, 4, 2, 3, 3, 7])
isEven = runner.isEvenOddTree(root)
assert isEven == False

root = TreeNode.init_from_list(TreeNode, [5, 9, 1, 3, 5, 7])
isEven = runner.isEvenOddTree(root)
assert isEven == False

root = TreeNode.init_from_list(
    TreeNode, [11, 12, 8, 3, 7, 11, None, None, None, 20])
root.print_tree()
isEven = runner.isEvenOddTree(root)
assert isEven == True
