# 125. Valid Palindrome

from test_helper import parse_example_to_test_case
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z0-9]', '', s.lower())
        return s == s[::-1]


example = """
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

if __name__ == "__main__":
    test_cases = parse_example_to_test_case(example)
    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        result = solution.isPalindrome(**test_case["args"])
        assert result == test_case["expected"], f"Test {i} failed! Expected {
            test_case['expected']}, but got {result}"
