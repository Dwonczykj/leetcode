from typing import List

import random
import math


'''
# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150)

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        # track the previous high and also add a curr_depth that we add to when next value right is less than previous value.
        debug = True
        if debug:
            print('\nNEW SOLUTION\n')

        def f(height: List[int]):
            if debug:
                print(f'\nNEW ITER: {height}\n')

            lagging_high_ind = 0
            lead_high_below_lag_high_ind = 0
            bowl = 0
            water = 0
            if not height or len(height) < 3:
                return 0, 0, 0, 0
            if debug:
                print(f'Prev at [{0}] with h: {height[0]}')
            for i in range(1, len(height)):
                if height[i] > height[i-1]:
                    if height[i] >= height[lagging_high_ind]:
                        # fill water
                        if debug and bowl > 0:
                            print(
                                f'Adding total water: {bowl}, total = {water + bowl} at index [{i}]')
                        water += bowl
                        bowl = 0
                        if debug:
                            print(f'Prev at [{i}] with h: {height[i]}')
                        lagging_high_ind = i
                    else:
                        if debug:
                            print(
                                f'Next lead high at [{i}] with h: {height[i]}')
                        lead_high_below_lag_high_ind = i
                        if debug:
                            print(
                                f'Add {height[lagging_high_ind] - height[i]} to current bowl at index [{i}]')
                        bowl += height[lagging_high_ind] - height[i]
                elif height[i] < height[i-1]:
                    if debug:
                        print(
                            f'Add {height[lagging_high_ind] - height[i]} to current bowl at index [{i}]')
                    bowl += height[lagging_high_ind] - height[i]
                else:
                    if debug:
                        print(
                            f'Add {height[lagging_high_ind] - height[i]} to current bowl at index [{i}]')
                    bowl += height[lagging_high_ind] - height[i]
            return water, bowl, lagging_high_ind, lead_high_below_lag_high_ind
        water, bowl, lagging_high_ind_fwd, lead_high_below_lag_high_ind_fwd = f(
            height)
        if bowl != 0 and lead_high_below_lag_high_ind_fwd > lagging_high_ind_fwd:
            rev_water, rev_bowl, lagging_high_ind_bwd, lead_high_below_lag_high_ind_fwd = f(
                height[:lagging_high_ind_fwd-1 if lagging_high_ind_fwd > 0 else None:-1])
            return water + rev_water
        else:
            return water

        # if bowl != 0 and lead_high_below_lag_high_ind > lagging_high_ind:
        #     # run backwards until bowl closes:
        #     bowl = 0
        #     for i in range(lead_high_below_lag_high_ind-1, -1, -1):
        #         if height[i] > height[lead_high_below_lag_high_ind]:
        #             break
        #         if debug:
        #             print(
        #                 f'[REVERSE] Add {height[lead_high_below_lag_high_ind] - height[i]} to current bowl at index [{i}]')
        #         bowl += height[lead_high_below_lag_high_ind] - height[i]
        #     if debug and bowl > 0:
        #         print(
        #             f'[REVERSE] Adding total water: {bowl}, total = {water + bowl} at index [{i}]')
        #     water += bowl

            # remove_above_bowl = (height[lagging_high_ind]-height[lead_high_below_lag_high_ind])*(
            #     lead_high_below_lag_high_ind-lagging_high_ind)

            # remove_strictly_after_bowl = \
            #     (sum([height[lagging_high_ind]-height[i] for i in range(lead_high_below_lag_high_ind+1, len(height))]) if
            #      (lead_high_below_lag_high_ind+1) < len(height) else 0)
            # if debug:
            #     print(
            #         f'Removing excess bowl water before adding to the total level at index [{i}]. bowl was {bowl} and removing {remove_above_bowl} above bowl [{lagging_high_ind}:{lead_high_below_lag_high_ind}] and {remove_strictly_after_bowl} strictly after bowl [{lead_high_below_lag_high_ind+1}:{len(height)}]')
            # bowl -= remove_above_bowl + remove_strictly_after_bowl
            # water += bowl
        if debug:
            print(
                f'Finished with prev at heights[{lagging_high_ind}]={height[lagging_high_ind]}')
            print(
                f'Finished with next at heights[{lead_high_below_lag_high_ind}]={height[lead_high_below_lag_high_ind]}')
        return water

    def trap_2walls(self, height: List[int]) -> int:

        i = 0
        left_max = height[0]
        sum = 0
        j = len(height) - 1
        right_max = height[j]
        while i < j:
            if left_max <= right_max:
                sum += left_max - height[i]
                i += 1
                left_max = max(left_max, height[i])
            else:
                sum += right_max - height[j]
                j -= 1
                right_max = max(right_max, height[j])
        return sum


runner = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output = runner.trap(height)
assert output == 6

height = [4, 2, 0, 3, 2, 5]
output = runner.trap(height)
assert output == 9

height = [5, 4, 1, 2]
output = runner.trap(height)
assert output == 1

height = [0, 1, 2, 0, 3, 0, 1, 2, 0, 0, 4, 2, 1, 2, 5, 0, 1, 2, 0, 2]
output = runner.trap(height)
assert output == 26

height = [9, 6, 8, 8, 5, 6, 3]
output = runner.trap(height)
assert output == 3

print('done')
