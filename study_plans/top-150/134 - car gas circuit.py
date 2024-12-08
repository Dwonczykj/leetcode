from typing import List

import random
import math

'''
URL: https://leetcode.com/problems/gas-station/description/?envType=study-plan-v2&envId=top-interview-150

134. Gas Station

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 
Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.

 
Constraints:

	n == gas.length == cost.length
	1 <= n <= 105
	0 <= gas[i], cost[i] <= 104
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # start at index 0 and see if that works
        n = len(gas)
        can_be_negative_tank = 0
        real_tank = 0
        starting_ind = 0
        # idea here is that if there is any way to get round all gas stations, then if we go do a full loop allowing the 
        # the tank to go negative, by the end the tank would be at least positive, meaning that there is a solution
        # then all we would need to do would be to find the station to start at so that we don't need to go into negative fuel.
        # to do this, we simply try starting at stations[i] until we find a run to station[n-1] that is not negative (
        # we don't need to check that we can go from station[n-1] to station[i] as 
        # we have already checked that you cannot start from any of stations[0:i] and we also know that there exists a solution)
        
        for i in range(n):
            real_tank += gas[i] - cost[i] # fill up at station i and then drive to station i+1 for cost[i]
            can_be_negative_tank += gas[i] - cost[i]
            if real_tank < 0:
                real_tank = 0
                starting_ind = i+1 # start from next station as all stations from 0,1,...,i [0:i+1] produce a -ve tank
        return -1 if can_be_negative_tank < 0 else starting_ind
            
        
        
        
        # n = len(gas)
        # i_start = 0
        # counter = 0
        # igas = gas[i_start]
        # passed_n = False

        # while counter < n:
        #     s = (i_start + counter) % n
        #     if s == n-1:
        #         passed_n = True
        #     if igas < cost[s]:
        #         # try restarting at s
        #         if i_start == n-1 or passed_n:
        #             return -1
        #         i_start = s + 1
        #         igas = gas[s+1]
        #         counter = 0
        #     else:
        #         igas += gas[(s+1) % n] - cost[s]
        #         if counter == n-1:
        #             return i_start
        #         counter += 1
        # return None
        
        # def get_range(start) -> list:
        #     return (range(start,n) + range(start))
        
        # while i_start < n:
        #     for i,s in enumerate(get_range(i_start)):
        #         if igas < cost[s]:
        #             # try restarting at s
        #             if s == n-1 or passed_n:
        #                 return -1
        #             i_start = s + 1
        #             igas = 0
        #             break
        #         igas += gas[s+1] - cost[s]
        #         if s == n-1:
        #             passed_n = True
        #         if i == n-1:
        #             return i_start
                

runner = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
output = runner.canCompleteCircuit(gas, cost)
assert output == 3

gas = [2,3,4]
cost = [3,4,3]
output = runner.canCompleteCircuit(gas, cost)
assert output == -1

debug = True


            
