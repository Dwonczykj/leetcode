from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        
        """
        i = 0
        for j in range(1,len(nums)):
            nums[j] # is it a second duplicate?
            if nums[j] == nums[i] and i > 0 and nums[j] != nums[i-1]:
                # this is second duplicate so insert into array
                i += 1
                nums[i] = nums[j]
            elif nums[j] == nums[i] and i == 0:
                # this is second duplicate so insert into array
                i += 1
                nums[i] = nums[j]
            elif nums[j] != nums[i]:
                # this must be a new unique
                i += 1
                nums[i] = nums[j]
        

        return i + 1
    # for each point in array at index i, search starting array for second duplicate value if exists, else next new value

            
                
                
            
        

runner = Solution()

# nums = [1,2]
# k = runner.removeDuplicates(nums)
# assert nums == [1,2]

# nums = [1,1,1]
# k = runner.removeDuplicates(nums)
# assert nums == [1,1,1]

nums = [1,1,1,5,5,5]
k = runner.removeDuplicates(nums)
assert nums == [1,1,5,5,5,5]

nums = [1,1,1,1,2,2,2,3,3,5,5]

k = runner.removeDuplicates(nums)
assert nums == [1,1,2,2,3,3,5,5]

nums = [1,1,1,1,2,3,3,5,5]
[1,1,2,1,3,3,5,5]
k = runner.removeDuplicates(nums)
assert nums == [1,1,2,2,3,3,5,5]

nums = [1,1,2,2,2,3,3,5,5]
k = runner.removeDuplicates(nums)
assert nums == [1,1,2,2,3,3,5,5]

nums = [1,1,2,2,2,3,3,5,5]
k = runner.removeDuplicates(nums)
assert nums == [1,1,2,2,3,3,5,5]

nums = [1,1,1,2,3,3,5,5]
k = runner.removeDuplicates(nums)
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