# 11. Container with the most water.
# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        maxArea = 0
        # start at the edges of the graph and move in one pointer at a time
        # using the strategy that if left pointer block is lower than right's
        # then move left up one, else move right down one which ensures we are
        # always getting the largest possble area for each combination of left and right.
        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea


if __name__ == "__main__":
    solution = Solution()

    # result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    # assert result == 49
    result = solution.maxArea([1, 2, 3, 4, 5, 25, 24, 3, 4])
    assert result == 24
