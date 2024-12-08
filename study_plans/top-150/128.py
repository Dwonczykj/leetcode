# 128. Longest Consecutive Sequence

from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(f"nums: {nums}")
        current = nums[0] - 1
        found = defaultdict(int)  # max int in sequence as key
        max_consec = 0
        for i, v in enumerate(nums):
            if i == 0 or v - current == 1:
                max_consec += 1
                current = v
                print(f"Set counter: [{max_consec}] on -> [{v}]")
            elif v > current:
                found[current] = max_consec
                print(
                    f"Saved counter:[{max_consec}] for max of sequence: [{current}]")
                current = v
                max_consec = 1
                print(f"reset counter at -> [{v}]")
        if current not in found:
            found[current] = max_consec
        return max(found.values())


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        # ({"nums": [1]}, 1),
        # ({"nums": [1, 2]}, 2),
        # ({"nums": [1, 2, 4]}, 2),
        ({"nums": [1, 2, 0, 1]}, 3),
        ({"nums": [-1, 0, 0]}, 2),
        ({"nums": [0, 3, 2, 0, 1]}, 4),
        ({"nums": [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]}, 9)
    ]
    for kwargs, expected in kwargs_list:
        result = sol.longestConsecutive(**kwargs)
        assert result == expected
