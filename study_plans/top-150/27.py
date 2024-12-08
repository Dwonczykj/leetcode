from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        p1 = 0
        while p1 < len(nums):
            if nums[p1] == val:
                del nums[p1]
                k -= 1
            else:
                p1 += 1
        return k

runner = Solution()

nums = [1,2,3,0,3,0]
val = 3
k = runner.removeElement(nums,val)
assert k == 4
assert nums == [1,2,0,0]

debug = True