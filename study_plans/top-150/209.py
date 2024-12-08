# 209 Minimum Size Subarray Sum

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        cur_sum = 0
        min_len = float("inf")
        if cur_sum >= target:
            return 1

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1
        return min_len if min_len != float("inf") else 0


if __name__ == "__main__":
    leet = 0
    sol = Solution()
    kwargs_list = [
        ({'target': 6, 'nums': [2, 3, 1, 1, 2, 4, 3, 4]}, 2),
        ({'target': 6, 'nums': [2, 3, 1, 1, 2, 4, 3, 4, 6]}, 1),
        ({'target': 11, 'nums': [1, 1, 1, 1, 1, 1, 1, 1]}, 0),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.minSubArrayLen(**kwargs)
        assert expected == result
