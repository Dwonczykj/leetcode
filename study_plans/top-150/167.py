# 167. Two Sum II - Input Array Is Sorted

from typing import List
from test_helper import parse_example_to_test_case


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            elif s > target:
                right -= 1
        return [-1, -1]


example = """
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

"""


if __name__ == "__main__":
    test_cases = parse_example_to_test_case(example)
    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        result = solution.isPalindrome(**test_case["args"])
        assert result == test_case["expected"], f"Test {i} failed! Expected {
            test_case['expected']}, but got {result}"
