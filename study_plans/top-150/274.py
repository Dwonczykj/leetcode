from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_sorted = list(sorted(citations, reverse=True))
        h = 0
        for i in range(len(citations)):
            # h from sorted citations so far is
            if citations_sorted[i] >= i + 1:
                h = i + 1
            else:
                return h
        return h

    
            
    

runner = Solution()

nums = [3,0,6,1,5]
# for all 0s in chain, the max jump beofre the zero must take us beyond the zero, i.e. one of the numbers before needs to have a value greater than jump to that 0
output = runner.hIndex(nums)
assert output == 3, "output should be 3"

nums = [1,3,1]
# for all 0s in chain, the max jump beofre the zero must take us beyond the zero, i.e. one of the numbers before needs to have a value greater than jump to that 0
output = runner.hIndex(nums)
assert output == 1, "output should be 1"



debug = True