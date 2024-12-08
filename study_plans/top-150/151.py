from typing import List


class Solution:

    def reverseWords(self, s: str) -> str:
        return " ".join([w for w in s.strip(' ').split(' ')[:None:-1] if w != ""])


runner = Solution()

assert runner.reverseWords("") == ""

print('Done')
