from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m = len(nums)
        # js = [(i + k) % m for i in range(m)]
        # def switch(i: int, j: int):
        #     temp = nums[i]
        #     nums[i] = nums[j]
        #     nums[j] = temp
        #     del temp
        #     return
        if k < 1:
            return
        new_front = nums[m-k:] + nums[:m-k]
        for i in range(m-k):
            nums[i] = new_front[i]
        return 

            
    

runner = Solution()

nums = [1,2,3,4,5,6,7]
k = 3
runner.rotate(nums, k)

debug = True