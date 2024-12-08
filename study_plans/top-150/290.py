# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lu = dict()
        count = 0
        for i, word in enumerate(s.split(' ')):
            if i >= len(pattern):
                return False
            if word in lu and lu[word] != pattern[i]:
                return False
            if pattern[i] in lu.values() and [k for k, v in lu.items() if v == pattern[i]][0] != word:
                return False
            lu[word] = pattern[i]
            count = i

        return count == len(pattern) - 1
