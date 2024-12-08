from collections import deque, defaultdict
from typing import List, Optional, Tuple, Set
from objects.binary_tree_node import TreeNode

import random
import math

'''
# [1530. Number of Good Leaf Nodes Pairs](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/?envType=daily-question&envId=2024-07-21)

You are given the `root` of a binary tree and an integer `distance`. A pair of two different **leaf**  nodes of a binary tree is said to be good if the length of **the shortest path**  between them is less than or equal to `distance`.

Return the number of good leaf node pairs in the tree.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/e1.jpg" style="width: 250px; height: 250px;">

```
Input: root = [1,2,3,None,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/e2.jpg" style="width: 250px; height: 182px;">

```
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
```

**Example 3:** 

```
Input: root = [7,1,4,6,None,5,3,None,None,None,None,None,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
```

**Constraints:** 

- The number of nodes in the `tree` is in the range `[1, 2^10].`
- `1 <= Node.val <= 100`
- `1 <= distance <= 10`
'''

# Definition for a binary tree node. - Moved to own file
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self) -> None:
        # The line `self.pairs:List[Tuple[int, int]] = []` in the `Solution` class is initializing an
        # instance variable `pairs` as an empty list that will hold tuples of integers. The type hint
        # `List[Tuple[int, int]]` indicates that `pairs` will be a list of tuples where each tuple
        # contains two integers. This variable is used to store the pairs of leaf nodes that satisfy
        # the condition of having a shortest path less than or equal to the given distance in the
        # binary tree.
        self.pairs: List[Tuple[int, int]] = []

    # https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/solutions/5493798/ultimate-1-ms-solution-beats-100-java-c-py-js-go-beginner-friendly-explanation
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = defaultdict(list)
        leaf_nodes = set()

        def traverse_tree(curr_node: Optional[TreeNode], prev_node: Optional[TreeNode]):
            """
            The function `traverse_tree` recursively traverses a binary tree, identifying leaf nodes and
            creating a graph representation of the tree.

            :param curr_node: The `curr_node` parameter represents the current node being traversed in a
            tree data structure. It is a reference to the node currently being visited during a tree
            traversal algorithm
            :param prev_node: The `prev_node` parameter in the `traverse_tree` function represents the
            parent node of the current node (`curr_node`) being traversed in a tree data structure. It
            is used to establish the parent-child relationship between nodes in the tree and to build a
            graph representation of the tree for further
            :return: The `traverse_tree` function does not explicitly return any value. It is a
            recursive function that traverses a tree and populates a set `leaf_nodes` and a graph
            `graph` based on the input `curr_node` and `prev_node`. The function modifies these data
            structures during its execution but does not return any specific value.
            """
            if not curr_node:
                return
            if not curr_node.left and not curr_node.right:
                leaf_nodes.add(curr_node)
            if prev_node:
                graph[prev_node].append(curr_node)
                graph[curr_node].append(prev_node)
            traverse_tree(curr_node.left, curr_node)
            traverse_tree(curr_node.right, curr_node)

        traverse_tree(root, None)

        ans = 0
        for leaf in leaf_nodes:
            bfs_queue = deque([leaf])
            seen = {leaf}
            for i in range(distance + 1):
                size = len(bfs_queue)
                for _ in range(size):
                    curr_node = bfs_queue.popleft()
                    if curr_node in leaf_nodes and curr_node != leaf:
                        ans += 1
                    for neighbor in graph[curr_node]:
                        if neighbor not in seen:
                            bfs_queue.append(neighbor)
                            seen.add(neighbor)

        return ans // 2

    def countPairs(self, root: TreeNode, distance: int) -> int:
        # calculate shortest_path algorithm from each leaf node
        # leaf nodes are all nodes that have no adjacent nodes
        # remove the source leaf nodes of pair when find a pair that satisfies this condition - and add this source node to visited so don't double count it when calculating from other leaf node
        # are there any optimisations that can be done during SPA for one source that we can infer shortest path for another source using the DFS pre and post visited labels
        parents: dict[TreeNode, TreeNode] = {}
        depths: dict[TreeNode, int] = {}
        leaf_nodes: Set[TreeNode] = set()
        leaf_nodes_seen = set()

        def children(node: TreeNode) -> List[TreeNode]:
            out = []
            if node.left:
                out.append(node.left)
                node.left.parent = node
            if node.right:
                out.append(node.right)
                node.right.parent = node
            if not node.left and not node.right:
                # node can be added to list of nodes twice
                leaf_nodes.add(node)
                leaf_nodes_seen.add(node.val)
            return out

        def dfs_trav(cur_depth: int, _node: TreeNode):
            depths[_node] = cur_depth
            _node.depth = cur_depth
            for cn in children(_node):
                parents[cn] = _node
                dfs_trav(cur_depth+1, cn)

        dfs_trav(0, root)

        # for 2 leaves of a pair that we want to check,
        # start counter at both leaves and go up the tree 1 level at a time for both leaves
        # until the parent node is the same, then we have the path == 2 * counter

        def get_distance(l: TreeNode, ol: TreeNode, parents: dict[TreeNode:TreeNode], depth: dict[TreeNode, int]):
            n1 = l
            n2 = ol
            c = 0
            while depth[n1] != depth[n2]:
                if depth[n1] > depth[n2]:
                    n1 = parents[n1]
                    c += 1
                else:
                    n2 = parents[n2]
                    c += 1
            while n1 != n2:
                n1 = parents[n1]
                n2 = parents[n2]
                c += 2
            return c

        counter = 0
        self.pairs = []
        l = leaf_nodes.pop() if leaf_nodes else None
        while l:
            for ol in leaf_nodes:
                d = get_distance(l, ol, parents, depths)
                if d <= distance:
                    counter += 1
                    self.pairs.append((l, ol))
            l = leaf_nodes.pop() if leaf_nodes else None
        return counter

    def dfs(self, node: TreeNode):
        visited: dict[TreeNode, int] = {}
        pre: dict[int, int] = {}
        post: dict[int, int] = {}
        traversal_index: dict[TreeNode, int] = {}

        # time = 1

        parents: dict[TreeNode, TreeNode] = {}
        depths: dict[TreeNode, int] = {}
        leaf_nodes = set()

        def children(node: TreeNode) -> List[TreeNode]:
            out = []
            if node.left:
                out.append(node.left)
                node.left.parent = node
            if node.right:
                out.append(node.right)
                node.right.parent = node
            if not node.left and not node.right:
                leaf_nodes.add(node)
            return out

        def dfs_trav(cur_depth: int, _node: TreeNode):
            depths[_node.val] = cur_depth
            for cn in children(_node):
                parents[cn] = _node
                dfs_trav(cur_depth+1, cn)

        dfs_trav(0, node)

        def sub_rec(time: int, _node: TreeNode, pre: dict[int, int], post: dict[int, int], visited: dict[TreeNode, int], trav_inds: dict[TreeNode, int]):
            # add _node to pre as only call sub_rec if not in visited

            pre[_node.val] = time
            if _node not in trav_inds:
                trav_inds[_node] = time
            time += 1
            visited[_node] = 1
            for cn in children(_node):
                parents[cn] = _node
                if cn not in visited:
                    sub_rec(time, cn, pre, post, visited, trav_inds)
            post[_node.val] = time
            time += 1

        sub_rec(0, node, pre, post, visited,  traversal_index)

        def is_ancestor(node: TreeNode, node_anc_potent: TreeNode, pre: dict[int, int], post: dict[int, int]):
            return pre[node_anc_potent.val] < pre[node.val] and post[node_anc_potent] > post[node.val]

    def shortest_path(self, node: TreeNode, distance: int):
        # record distance to each node in a list
        new_nodes = [node]
        path_length = 0
        shortest_paths = {}
        leaf_nodes = set()
        all_nodes = [node]
        vis_pre = []
        vis_post = []
        while new_nodes:
            next_nodes = []
            for node in new_nodes:
                shortest_paths[node] = path_length
                if node.left:
                    next_nodes.append(node.left)
                    all_nodes.append(node.left)
                else:
                    all_nodes.append(None)
                if node.right:
                    next_nodes.append(node.right)
                    all_nodes.append(node.right)
                else:
                    all_nodes.append(None)
                if not node.left and not node.right:
                    leaf_nodes.add(node)
            path_length += 1
            new_nodes = next_nodes

        # for 2 leaves of a pair that we want to check,
        # start counter at both leaves and go up the tree 1 level at a time for both leaves
        # until the parent node is the same, then we have the path == 2 * counter

        def get_distance(l: TreeNode, ol: TreeNode, parents: dict[TreeNode:TreeNode], depth: dict[TreeNode, int]):
            n1 = l
            n2 = ol
            c = 0
            while depth[n1] != depth[n2]:
                if depth[n1] > depth[n2]:
                    n1 = parents[n1]
                    c += 1
                else:
                    n2 = parents[n2]
                    c += 1
            while n1.val != n2.val:
                n1 = parents[n1]
                n2 = parents[n2]
                c += 2
            return c

        counter = 0
        pairs = []
        l = leaf_nodes.pop()
        while l:
            for ol in leaf_nodes:
                d = get_distance(l, ol)
                if d < distance:
                    counter += 1
                    pairs.append((l, ol))
            l = leaf_nodes.pop()
        return counter

        # use the 2^0 + 2^1 + ... code to calculate distance between leaf nodes
        # for each leaf node, to get distance to another leaf node:
        # get index of both in all nodes


runner = Solution()
root = TreeNode.init_from_list(TreeNode, [1, 2, 3, None, 4])
distance = 3
pairs = runner.countPairs(root, distance)
assert pairs == 1

root = TreeNode.init_from_list(TreeNode, [19, 10, 64, 75, 5, 68, 64, 53, 35, 63, 53, 76, 45, 48, 6, 13, 31, 8, 72, 10, 79, 9, 96, 45, None, None, 63, 7, 65, None, 7, 35, 74, None, None, 56, None, 70, 41, None,
                               None, 64, None, None, None, None, None, None, None, 86, 97, None, None, None, None, None, None, 53, 67, None, None, 98, None, None, None, None, None, None, None, None, None, 34, None, None, None, 64, None, 62])
root.print_tree()
distance = 1
pairs = runner.countPairs(root, distance)
assert pairs == 0
