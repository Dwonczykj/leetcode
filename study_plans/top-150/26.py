from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

        Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
        Return k.
        """
        
        # if not nums:
        #     return 0
        # p1 = 0
        # while p1 < len(nums) - 1:
        #     if nums[p1] == nums[p1+1]:
        #         del nums[p1+1]
        #     else:
        #         p1 += 1
        # return p1 + 1
        
        ## solution 2
        # L=1

        # for R in range(1,len(nums)):
        #     if (nums[R]!=nums[R-1]):
        #         nums[L]=nums[R]
        #         L+=1

        # return L

        ## Solution 3
        # if not nums:
        #     return 0
    
        # slow_ptr = 0
    
        # for fast_ptr in range(1, len(nums)):
        #     if nums[fast_ptr] != nums[slow_ptr]:
        #         slow_ptr += 1
        #         nums[slow_ptr] = nums[fast_ptr]
    
        # return slow_ptr + 1  

        ## Solution 4 - Mine
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

runner = Solution()

nums = [1,2,2,3,3,5,5]
k = runner.removeDuplicates(nums)
assert k == 4
assert nums[:4] == [1,2,3,5]

debug = True

nums = [1,2,5,5]
k = runner.removeDuplicates(nums)
assert k == 3
assert nums[:4] == [1,2,5]

debug = True