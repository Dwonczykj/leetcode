# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/submissions/1471373989/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict
from typing import List
from icecream import ic


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        My strategy needs two lines. 
        Reflect in horizontal then in NW to SE diagonal. 

        The first line should be center of image horizontally.

        1,2,3
        -----
        7,8,9
        Swap numbers above and below. That means

        Swap 1 and 7
        Swap 2 and 8
        Swap 3 and 9

        In the end,

        7,8,9
        4,5,6
        1,2,3
        The second line should on the 7, 5 and 3.

        *,8,9
        4,*,6
        1,2,*
        Swap 8 and 4
        Swap 9 and 1
        Swap 6 and 2

        In the end,

        7,4,1
        8,5,2
        9,6,3
        Easy!😃
        """
        n = len(matrix)

        top = 0
        bottom = n - 1

        def swap(ind1: tuple[int, int], ind2: tuple[int, int]):
            temp = matrix[ind2[0]][ind2[1]]
            matrix[ind2[0]][ind2[1]] = matrix[ind1[0]][ind1[1]]
            matrix[ind1[0]][ind1[1]] = temp

        while top < bottom:
            for j in range(n):
                swap((top, j), (bottom, j))
            top += 1
            bottom -= 1

        for i in range(n):
            for j in range(i+1, n):
                # columns greater than i means north east of diagonal line
                swap((i, j), (j, i))
        return None


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        ({"matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]},
         [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.rotate(**kwargs)
        assert result == expected
