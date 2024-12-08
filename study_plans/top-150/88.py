from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2.pop(0)

        for i in range(m + n):
            if len(nums2) < 1:
                return
            
            if nums2 and nums2[0] < nums1[i]:
                temp = nums1[i]
                nums1[i] = nums2.pop(0)
                if i + 1 < m + n:
                    nums1.insert(i+1, temp)
                    nums1.pop(-1)
                
        if len(nums2) > 0:
            f = n - len(nums2)
            for i in range(m + f, m + n):
                nums1[i] = nums2.pop(0)

runner = Solution()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

runner.merge(nums1,m,nums2,n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1

runner.merge(nums1,m,nums2,n)
print(nums1)

nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3

runner.merge(nums1,m,nums2,n)
print(nums1)
assert nums1 == [-1,0,0,1,2,2,3,3,3]

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5

runner.merge(nums1,m,nums2,n)
print(nums1)
assert nums1 == [1,2,3,4,5,6]

nums1 = [-4,4,0,0,0,0,0]
m = 2
nums2 = [1,2,3,5,6]
n = 5

runner.merge(nums1,m,nums2,n)
print(nums1)
assert nums1 == [-4,1,2,3,4,5,6]

                