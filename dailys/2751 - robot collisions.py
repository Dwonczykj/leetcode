from typing import List

import random
import math

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        def get_next_collisions():
            colisions = [0] * (n-1)
            for i in range(n-1):
                if positions[i] == positions[i+1] - 1 and directions[i] != directions[i+1]\
                    and healths[i] > 0 and healths[i+1] > 0:
                    colisions[i] = 1
            for i in range(n):
                if colisions[i] > 0:
                    if healths[i] > healths[i+1]:
                        healths[i] = healths[i] - healths[i+1]
                        healths[i+1] = -1
                    elif healths[i] < healths[i+1]:
                        healths[i+1] = healths[i+1] - healths[i]
                        healths[i] = -1
                    else:
                        healths[i] = -1
                        healths[i+1] = -1


    
            
    

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