from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        for i in range(n-1):
            if nums[i] == 0:
                can_pass_this_zero = False
                for j,v in enumerate(nums[0:i]):
                    if v > (i - j):
                        can_pass_this_zero = True
                        continue
                if not can_pass_this_zero:
                    print(f'cannot get past zero at index [{i}]')
                    return False
        return True
    
            
    

runner = Solution()

nums = [3,2,1,0,4]
# for all 0s in chain, the max jump beofre the zero must take us beyond the zero, i.e. one of the numbers before needs to have a value greater than jump to that 0
output = runner.canJump(nums) # False
assert output == False, "output should be false"

debug = True