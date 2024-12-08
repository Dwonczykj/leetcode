from collections import deque, defaultdict
from typing import List, Optional, Tuple

import random
import math

'''
# [2392. Build a Matrix With Conditions](https://leetcode.com/problems/build-a-matrix-with-conditions/description/?envType=daily-question&envId=2024-07-21)

You are given a **positive**  integer `k`. You are also given:

- a 2D integer array `rowConditions` of size `n` where `rowConditions[i] = [above<sub>i</sub>, below<sub>i</sub>]`, and
- a 2D integer array `colConditions` of size `m` where `colConditions[i] = [left<sub>i</sub>, right<sub>i</sub>]`.

The two arrays contain integers from `1` to `k`.

You have to build a `k x k` matrix that contains each of the numbers from `1` to `k` **exactly once** . The remaining cells should have the value `0`.

The matrix should also satisfy the following conditions:

- The number `above<sub>i</sub>` should appear in a **row**  that is strictly **above**  the row at which the number `below<sub>i</sub>` appears for all `i` from `0` to `n - 1`.
- The number `left<sub>i</sub>` should appear in a **column**  that is strictly **left**  of the column at which the number `right<sub>i</sub>` appears for all `i` from `0` to `m - 1`.

Return **any**  matrix that satisfies the conditions. If no answer exists, return an empty matrix.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2022/07/06/gridosdrawio.png" style="width: 211px; height: 211px;">

```
Which shows _ _ _ _ _
           | 3  0  0 |
           | 0  0  1 |
           | 0  2  0 |
            _ _ _ _ _
Input: k = 3, 
    rowConditions = [[1,2],[3,2]], # 1 needs to be in a higher row than 2 and 3 needs to be in a higher row than 2 
    colConditions = [[2,1],[3,2]] 2 needs to be in a further left column than 1 and 3 needs to be further left than 2
    i.e the 
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.
```

**Example 2:** 

```
Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.
```

**Constraints:** 

- `2 <= k <= 400`
- `1 <= rowConditions.length, colConditions.length <= 10^4`
- `rowConditions[i].length == colConditions[i].length == 2`
- `1 <= above<sub>i</sub>, below<sub>i</sub>, left<sub>i</sub>, right<sub>i</sub> <= k`
- `above<sub>i</sub> != below<sub>i</sub>`
- `left<sub>i</sub> != right<sub>i</sub>`
'''


class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        # return True if all okay and return False if cycle was found
        def dfs(src, graph, visited, cur_path, res) -> bool:
            if src in cur_path:
                return False  # cycle detected

            if src in visited:
                return True  # all okay, but we've already visited this node

            visited.add(src)
            cur_path.add(src)

            for neighbor in graph[src]:
                if not dfs(neighbor, graph, visited, cur_path, res):  # if any child returns false
                    return False

            cur_path.remove(src)  # backtrack path
            res.append(src)
            return True

        # if there will be cycle - return empty array, in other case return 1d array as described above
        def topo_sort(edges) -> list[int]:
            # The above code snippet is creating an empty defaultdict named `graph` in Python. This
            # defaultdict will store lists as values for each key.
            # The above code snippet is creating an empty defaultdict named `graph` in Python. This
            # defaultdict will store lists as values for each key.
            graph = defaultdict(list)
            for src, dst in edges:
                graph[src].append(dst)

            visited: set[int] = set()
            cur_path: set[int] = set()
            res: list[int] = []

            for src in range(1, k + 1, 1):
                if not dfs(src, graph, visited, cur_path, res):
                    return []

            # we will have res as reversed so we need to reverse it one more time
            return res[::-1]

        row_sorting: list[int] = topo_sort(rowConditions)
        col_sorting: list[int] = topo_sort(colConditions)
        if [] in (row_sorting, col_sorting):
            return []

        value_position: dict[int, list[int]] = {
            n: [0, 0] for n in range(1, k + 1, 1)
        }  # element -> [row_index, col_index]
        for ind, val in enumerate(row_sorting):
            value_position[val][0] = ind
        for ind, val in enumerate(col_sorting):
            value_position[val][1] = ind

        res: list[list[int]] = [[0 for _ in range(k)] for _ in range(k)]
        for value in range(1, k + 1, 1):
            row, column = value_position[value]
            res[row][column] = value

        return res

    def get_coords(self, output: List[List[int]], v: int) -> Tuple[int, int]:
        for i in range(k):
            if v in output[i]:
                return (i, output[i].index(v))
        else:
            raise ValueError(f'Could not locate {v} in output')

    def run_checks(self, k: int, output: List[List[int]], rowConditions: List[List[int]], colConditions: List[List[int]]) -> bool:
        for i in range(len(rowConditions)):
            above_coords = self.get_coords(output, rowConditions[i][0])
            below_coords = self.get_coords(output, rowConditions[i][1])
            ...

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def order_constraints(orderConditions: List[List[int]]):
            constraints: List[Tuple[List[int], List[int]]] = []
            resList = []
            for kk in range(1, k+1):
                befores = []
                afters = []
                for i in range(len(orderConditions)):
                    if orderConditions[i][0] == kk:
                        afters.append(orderConditions[i][1])
                    elif orderConditions[i][1] == kk:
                        befores.append(orderConditions[i][0])
                constraints.append((befores, afters))
            changes = True
            while changes == True:
                changes = False
                for kk in range(1, k+1):
                    befores = constraints[kk-1][0]
                    afters = constraints[kk-1][1]
                    len_b = len(befores)
                    len_a = len(afters)
                    for kkb in befores:
                        befores += constraints[kkb-1][0]
                        befores = list(set(befores))
                        constraints[kk-1] = (befores, afters)
                        if len(befores) > len_b:
                            changes = True

                    for kka in afters:
                        afters += constraints[kka-1][1]
                        afters = list(set(afters))
                        constraints[kk-1] = (befores, afters)
                        if len(afters) > len_a:
                            changes = True

            a = 0
            b = 0
            while a < k:
                for kk in range(1, k+1):
                    if len(constraints[kk-1][0]) == b:
                        # check that none of constraints[kk-1][0] are alrady in resList
                        if any((c in resList for c in constraints[kk-1][1])):
                            return []
                        resList.append(kk)
                        a += 1
                b += 1
            return resList

            # def get_numbers_before(kk:int, loop = 0):
            # # for kk in range(1,k+1):
            #     befores = constraints[kk-1][0]
            #     # afters = constraints[kk-1][1]
            #     for b in befores:
            #         if kk in constraints[b-1][0]:
            #             return []
            #     return [get_numbers_before(b) for b in befores]

            # resList = orderConditions[0]
            # skipped = []
            # for i in range(1, len(orderConditions)):
            #     if orderConditions[i][0] in resList and orderConditions[i][1] in resList:
            #         topInd = resList.index(orderConditions[i][0])
            #         bottomInd = resList.index(orderConditions[i][1])
            #         if bottomInd < topInd:
            #             return []
            #     elif orderConditions[i][0] in resList:
            #         topInd = resList.index(orderConditions[i][0])
            #         resList = resList[:topInd+1] + [orderConditions[i][1]] + resList[topInd +
            #                                                                          1:] if topInd < len(resList)-1 else resList + [orderConditions[i][1]]
            #     elif orderConditions[i][1] in resList:
            #         bottomInd = resList.index(orderConditions[i][1])
            #         resList = resList[:bottomInd] + [orderConditions[i][0]] + resList[bottomInd:] if bottomInd > 0 else [
            #             orderConditions[i][0]] + resList
            #     else:
            #         skipped.append(i)
            # for ii, i in enumerate(skipped):
            #     if orderConditions[i][0] in resList and orderConditions[i][1] in resList:
            #         topInd = resList.index(orderConditions[i][0])
            #         bottomInd = resList.index(orderConditions[i][1])
            #         if bottomInd < topInd:
            #             return []
            #         # make sure it is before rowConditions[i][1] in list
            #         # resList = resList[:bottomInd] + [orderConditions[i]
            #         #                                      [0]] + resList[bottomInd:topInd] + resList[topInd:]
            #     elif orderConditions[i][0] in resList:
            #         topInd = resList.index(orderConditions[i][0])
            #         resList = resList[:topInd+1] + [orderConditions[i][1]] + resList[topInd +
            #                                                                          1:] if topInd < len(resList)-1 else resList + [orderConditions[i][1]]
            #     elif orderConditions[i][1] in resList:
            #         bottomInd = resList.index(orderConditions[i][1])
            #         resList = resList[:bottomInd] + [orderConditions[i][0]] + resList[bottomInd:] if bottomInd > 0 else [
            #             orderConditions[i][0]] + resList
            #     else:
            #         resList = orderConditions[i] + resList

            # return resList
        rowList = order_constraints(orderConditions=rowConditions)
        if not rowList:
            return []
        colList = order_constraints(orderConditions=colConditions)
        if not colList:
            return []
        outarray = [[0]*k for _ in range(k)]
        for i, v in enumerate(rowList):
            j = colList.index(v)
            outarray[i][j] = v

        return outarray


runner = Solution()

k = 3
# rowConditions = [[1, 2], [3, 2]]
# colConditions = [[2, 1], [3, 2]]
# output = runner.buildMatrix(k, rowConditions, colConditions)
# assert output == [[3, 0, 0], [0, 0, 1], [0, 2, 0]
#                   ] or output == [[1, 0, 0], [3, 0, 0], [0, 2, 0]]

# k = 3
# rowConditions = [[1, 2], [2, 3], [3, 1], [2, 3]]
# colConditions = [[2, 1]]
# output = runner.buildMatrix(k, rowConditions, colConditions)
# assert output == []

k = 8
rowConditions = [[1, 2], [7, 3], [4, 3], [5, 8], [7, 8], [8, 2], [
    5, 8], [3, 2], [1, 3], [7, 6], [4, 3], [7, 4], [4, 8], [7, 3], [7, 5]]
colConditions = [[5, 7], [2, 7], [4, 3], [6, 7], [4, 3], [2, 3], [6, 2]]
output = runner.buildMatrix(k, rowConditions, colConditions)
assert output == [[0, 0, 0, 0, 0, 0, 7, 0], [0, 6, 0, 0, 0, 0, 0, 0], [0, 0, 5, 0, 0, 0, 0, 0], [0, 0, 0, 4, 0, 0, 0, 0], [
    8, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 2, 0, 0, 0]]

print('Done')
