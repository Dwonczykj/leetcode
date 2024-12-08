from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
            
    

runner = Solution()

nums = [1]
runner.majorityElement(nums)

debug = True