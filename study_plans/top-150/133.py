#  133. Clone Graph
#  https://leetcode.com/problems/clone-graph/description/?envType=study-plan-v2&envId=top-interview-150

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from pprint import pformat
from typing import Optional
from graph import Node
from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        q_origs, clones = deque([node]), {node.val: Node(node.val, [])}
        while q_origs:
            cur = q_origs.popleft()
            cur_clone = clones[cur.val]
            for neighbour in cur.neighbors:
                if neighbour.val not in clones:
                    clones[neighbour.val] = Node(neighbour.val, [])
                    q_origs.append(neighbour)
                cur_clone.neighbors += [clones[neighbour.val]]
        return clones[node.val]


if __name__ == "__main__":
    sol = Solution()
    null = None
    kwargs_list = [
        ({"node":
            [[2, 4], [1, 3], [2, 4], [1, 3]]},
            [[2, 4], [1, 3], [2, 4], [1, 3]]),
    ]
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        node = Node.init_from_list(kwargs["node"])
        result = sol.cloneGraph(node=node)
        y = result.to_adjacency_list()
        assert y == expected, f"Test {test_number}. Failed 🚨.\n{
            y}\n"+("!="*15)+f"{expected}"
        print(f"Test {test_number}. Passed ✅")
