from typing import List

import random
import math

print(random.randrange(1,10))

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''

class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        curr = 1
        result = [1]*n
        # deliberately skip result[0], we will get this on the second reverse loop where curr then will be all nums[n-1:0:-1]
        for i in range(1,n):
            result[i] = curr * nums[i-1]
            curr *= nums[i-1]
        
        curr = 1
        for i in range(n-2,-1,-1):
            result[i] = result[i] * curr * nums[i+1]
            curr *= nums[i+1]
        return result
        
        # cumprod = 1
        # results = []
        # for i in range(len(nums)):
        #     results.append(cumprod * math.prod(nums[i+1:]))
        #     cumprod *= nums[i]
        # return results
        
        # print([(nums[:i]+nums[i+1:]) for i in range(len(nums))])
        # return [math.prod(nums[:i]+nums[i+1:]) for i in range(len(nums))]
        
runner = Solution()
nums = [1,2,3,4]
output = runner.productExceptSelf(nums)
assert output == [24,12,8,6]

nums = [-1,1,0,-3,3]
output = runner.productExceptSelf(nums)
assert output == [0,0,9,0,0]

print('done')