# 200. Number of islands
# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

from collections import deque
from typing import List
from pprint import pprint, pformat


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        seen: set[tuple[int, int]] = set()

        n = len(grid)
        m = len(grid[0])
        islands_count = 0
        for i in range(n):
            for j in range(m):
                if (i, j) in seen:
                    continue

                seen.add((i, j))

                if grid[i][j] == "0":
                    continue

                # must be a new island as not in seen
                islands_count += 1
                print(f"Starting new island at [{i},{j}]")
                # now reveal all ones in this island and record their locations in seen
                q: deque[tuple[int, int]] = deque([(i, j)])
                while q:
                    k, l = q.pop()
                    # only look right and down as we have already covered the left and up by definition.
                    for t in [(k-1, l), (k, l-1), (k+1, l), (k, l+1)]:
                        if t[0] < n and t[0] >= 0 and t[1] >= 0 and t[1] < m and t not in seen and grid[t[0]][t[1]] == "1":
                            q.append(t)
                        seen.add(t)
        return islands_count


if __name__ == "__main__":
    from pprint import pformat, pprint
    sol = Solution()
    null = None
    kwargs_list = [
        ({"grid": [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]], }, 1),
        ({"grid": [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]], }, 3),
        ({"grid": [
            ["1", "1", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "1", "1", "1"]], }, 2),
        ({"grid": [
            ["1", "1", "1", "1", "0", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1"],
            ["0", "0", "1", "1", "0", "0", "1"],
            ["0", "0", "0", "0", "1", "1", "1"]], }, 1),
    ]
    test_number = 0
    for kwargs, expected in kwargs_list:
        test_number += 1
        print(
            "-"*30+f"\nNew Solution {test_number}.: {pformat(kwargs, indent=2)}")
        result = sol.numIslands(**kwargs)
        assert result == expected, f"Test {test_number}. Failed 🚨.\n{
            result}\n"+("!="*15)+f"{expected}"
        print(f"Test {test_number}. Passed ✅")
