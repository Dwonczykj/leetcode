from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0
        for c in s[:None:-1]:
            if c == " ":
                if out == 0:
                    continue
                else:
                    return out
            else:
                out += 1
        return out

    def lengthOfLastWord_simple(self, s: str) -> int:
        return len(s.rstrip(" ").split(" ")[-1])


runner = Solution()

s = "Hello World"
assert runner.lengthOfLastWord(s) == 5
s = "   fly me   to   the moon  "
assert runner.lengthOfLastWord(s) == 4
s = "luffy is still joyboy"
assert runner.lengthOfLastWord(s) == 6

print('Done')
