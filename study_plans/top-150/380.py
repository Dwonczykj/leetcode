from typing import List

import random
import math

print(random.randrange(1,10))

class RandomizedSet:


    def __init__(self):
        self._values = set()
        pass

    def insert(self, val: int) -> bool:
        if val in self._values:
            return False
        self._values.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self._values:
            self._values.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(tuple(self._values))

    
            
    

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