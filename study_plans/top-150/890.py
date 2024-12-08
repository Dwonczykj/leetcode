# 890 Find and replace pattern

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        out: List[str] = []
        n = len(pattern)
        for w in words:
            lu = dict()
            res = True
            for i in range(n):
                if w[i] in lu and lu[w[i]] != pattern[i]:
                    res = False
                    break
                elif pattern[i] in lu.values() and [k for k, v in lu.items() if v == pattern[i]][0] != w[i]:
                    res = False
                    break
                else:
                    lu[w[i]] = pattern[i]
            if res:
                out.append(w)
        return out


if __name__ == "__main__":
    sol = Solution()
    result = sol.findAndReplacePattern()
