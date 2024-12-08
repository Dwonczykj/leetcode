# 15. 3Sum
# https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        matches3: List[List[int]] = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                # as we just calculated the triplets for this iteration of nums[i] in the previous iteration.
                continue

            # start at edges of remaining items where we only allow left up and right down.
            # we can ignore all v in nums up to and including nums[i] because
            # for all of these numbers, we already find ALL the triplets
            # involving that starting number, therefore if we were to continue
            # to include them then they would definitely be duplicates
            left, right = i+1, len(nums) - 1
            while left < right:
                total = (nums[i] + nums[left] + nums[right])
                if total < 0:
                    # increase left pointer to make the nums[left] bigger
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    matches3.append(
                        [nums[i], nums[left], nums[right]])
                    # this removes duplicates within our same search for all triplets that start with nums[i]
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return matches3
