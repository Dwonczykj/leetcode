# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rPtr = 0
        mPtr = 0
        while mPtr < len(magazine):
            if magazine[mPtr] == ransomNote[rPtr]:
                rPtr += 1
                if rPtr == len(ransomNote):
                    return True
                magazine = magazine[:mPtr] + \
                    (magazine[mPtr+1:] if mPtr < len(magazine) else "")
                mPtr = 0
            else:
                mPtr += 1
        return False


if __name__ == "__main__":
    sol = Solution()
    result = sol.canConstruct("aa", "aab")
    assert result == True
