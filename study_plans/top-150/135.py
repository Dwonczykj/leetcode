from typing import List

import random
import math

print(random.randrange(1, 10))

'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 

Constraints:

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
'''


class Solution:
    def candy(self, ratings: List[int]) -> int:

        # TODO: Is there a simpler solution that goes through ratings once not caring if next one (right neighbour) is smaller
        # and just keeps on checking if bigger than previous, add one i.e.candies[i-1]+1  and append this value to candies array
        # then go in reverse on ratings and check candies are fine, if [i] < [i+1] prev rating in reverse, then correct it to max(candies[i],candies[i+1]+1)
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

    def candy(self, ratings: List[int]) -> int:
        # worst case is that you need to provide more and more candies: [1,2,3,4]
        # 1,3,2,3 -> 1,2,1,2 from 0,1,-1,1
        # 1,3,2,1,3 -> 1,3,2,1,2 from 0,1,-1,-1,1 where if we cumsum -> ind[3] is min, so start 1 there
        # 1,3,9,8,9,1 -> 1,2,3,1,2,1
        # RULE 1; if lower that all neighbours, use 1 candy
        # RULE 2: if higher than both neighbours, use max(neighbours candies) + 1
        # RULE 3: if between neighbours, use min(neighbours candies) + 1

        # Alternatively
        # RULE 1; if lower that left neighbour, add 1 candy and slope = -1 if slope >=0 else slope = slope - 1
        # RULE 2: if higher than left neighbour, add (1 * length of 'positive' slope) candy
        # RULE 3: if = to left neighbour, slope = 0
        # RULE 4: man handle the first case as it has no left neighbour.
        # RULE 4.1, if [0] <= [1] [0] = 1 (add 1 to output counter) else if [0] > [1] => add 1 to output counter and if it continues to be a negative slope we just need to add a 2 to next negative cunter step etc reflecting 2,1 and then if third lower neighbur, add 3 reflecting 3,2,1

        # 3,2,1,... 1. output = 1 => 2. 2 < 3 and 2 > 1 so min both neighbours candies is min of (1,tbc)
        # 1,2,3,...
        # 1,2,1,...
        # 1,2,3,4,4,4,3,5, -> 1,2,3,4,1,1,1,2 with slopes = [*0*,1,2,3,0,0,-1,1]
        # 3,1 -> 2,1 with slopes [*0*,-1] => man handle the first and last edge cases.
        # 8,9,4,3,2,1 -> 1,5,4,3,2,1
        # 4,3,2,2,3,1,3 -> 3,2,1,1,2,1,2

        output = 1
        slope = 0
        # history = [output]
        prev_high = 0
        for i in range(1, len(ratings)):
            if ratings[i] == ratings[i-1]:  # 0ve slope
                if slope < 0 and prev_high != 0:
                    output += max(-1*(prev_high + slope - 1), 0)
                    prev_high = 0
                output += 1
                slope = 0
            elif ratings[i] < ratings[i-1]:  # -ve slope
                if slope == 0:
                    slope = -2
                elif slope < 0:
                    slope -= 1
                else:
                    prev_high = slope
                    slope = -1
                output += abs(slope)
            elif ratings[i] > ratings[i-1]:  # +ve slope
                if slope == 0:
                    slope = 2
                elif slope > 0:
                    slope += 1
                else:
                    if prev_high != 0:
                        output += max(-1*(prev_high + slope - 1), 0)
                        prev_high = 0
                    slope = 2
                output += abs(slope)
            else:  # neutral (flat) slope
                raise Exception('Can\'t get here')
            # history.append(output)
        if prev_high != 0:
            output += max(-1*(prev_high + slope - 1), 0)
            prev_high = 0
        # print(history)
        return output


runner = Solution()
ratings = [1, 0, 2]
output = runner.candy(ratings)
assert output == 5

ratings = [1, 2, 2]
output = runner.candy(ratings)
assert output == 4

ratings = [4, 3, 2, 2, 3, 1, 3]
output = runner.candy(ratings)
assert output == sum([3, 2, 1, 1, 2, 1, 2])

ratings = [1, 6, 10, 8, 7, 3, 2]
output = runner.candy(ratings)
assert output == 18
assert output == sum([1, 2, 5, 4, 3, 2, 1])

print('done')
