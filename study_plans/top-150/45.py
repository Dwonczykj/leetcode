from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # start at the end - 1, can we reach the end in one jump from here? if so why? / how?
        n = len(nums)
        if n == 1:
            return 0
        steps_to_ends = [0 for _ in nums]
        for i in range(n-2,-1,-1):
            jump_total = n-1 - i
            if nums[i] >= jump_total:
                steps_to_ends[i] = 1
            elif nums[i] == 0:
                steps_to_ends[i] = 0
            else:
                print(f'steps_to_end[{i}] is min of {[1 + steps_to_ends[i+k] for j,k in enumerate(range(1,min(nums[i]+1,n-i))) if steps_to_ends[i+k] > 0]}')
                poss_steps = [1 + steps_to_ends[i+k] for j,k in enumerate(range(1,min(nums[i]+1,n-i))) if steps_to_ends[i+k] > 0]
                if poss_steps:
                    steps_to_ends[i] = min(poss_steps)
                else:
                    steps_to_ends[i] = 0

        print(nums)
        print(steps_to_ends)
        return steps_to_ends[0]
    
            
    

runner = Solution()

nums = [1,2,1,1,1]
# for all 0s in chain, the max jump beofre the zero must take us beyond the zero, i.e. one of the numbers before needs to have a value greater than jump to that 0
output = runner.jump(nums)
assert output == 3, "output should be 3"

nums = [2,3,0,1,4]
# for all 0s in chain, the max jump beofre the zero must take us beyond the zero, i.e. one of the numbers before needs to have a value greater than jump to that 0
output = runner.jump(nums)
assert output == 2, "output should be 2"



debug = True