# leetcode#. 228. Summary Ranges

from collections import defaultdict
from typing import List
from icecream import ic


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        lwr = 0
        upr = 0
        out: list[str] = []
        while i < len(nums):
            if i == 0 or nums[i] - nums[i-1] == 1:
                upr = i
            else:
                out.append(f"{nums[lwr]}->{nums[upr]}" if upr >
                           lwr else f"{nums[lwr]}")
                lwr = i
                upr = i
            i += 1
        if len(nums) > upr:
            out.append(f"{nums[lwr]}->{nums[upr]}" if upr >
                       lwr else f"{nums[lwr]}")
        return out


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        ({"nums": [0]}, ["0"]),
        ({"nums": [0, 1, 2, 4, 5, 7]}, ["0->2", "4->5", "7"]),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.summaryRanges(**kwargs)
        assert result == expected
