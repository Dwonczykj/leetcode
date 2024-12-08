# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150

# fileBasename. Longest Consecutive Sequence

from collections import defaultdict
from typing import List
from icecream import ic


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True

    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        # check rows are valid
        for i in range(9):
            s = set()
            for v in board[i]:
                if v == ".":
                    continue
                elif v in s:
                    return False
                s.add(v)

        # check columns are valid
        for j in range(9):
            s = set()
            for v in [l[j] for l in board]:
                if v == ".":
                    continue
                elif v in s:
                    return False
                s.add(v)
        # check boxes are valid
        for ki in range(3):
            for kj in range(3):
                s = set()
                vs = [board[k][ki*3:ki*3+3] for k in range(kj*3, kj*3+3)]
                vs = [c for l in vs for c in l]
                for v in vs:
                    if v == ".":
                        continue
                    elif v in s:
                        return False
                    s.add(v)

        return True


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        ({"board": [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
         ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]}, True),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.isValidSudoku(**kwargs)
        assert result == expected
