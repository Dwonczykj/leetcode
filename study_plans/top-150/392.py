# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_t = 0
        ptr_s = 0
        if not s and not t:
            return True
        elif s and not t:
            return False
        elif t and not s:
            return True
        while ptr_t < len(t):
            if ptr_s == len(s):
                return True
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1
        # crucial incase subsequence is in the last character of t.
        return ptr_s == len(s)
