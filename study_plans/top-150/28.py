# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150)
from test_helper import parse_example_to_test_case


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


example1 = """
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

# Test the solution
if __name__ == "__main__":
    test_cases = parse_example_to_test_case(example1)
    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        result = solution.strStr(**test_case["args"])
        assert result == test_case["expected"], f"Test {i} failed! Expected {
            test_case['expected']}, but got {result}"

    print("All tests passed!")
