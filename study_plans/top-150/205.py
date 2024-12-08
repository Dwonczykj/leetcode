# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lu_fwd = dict()
        lu_back = dict()

        for i in range(len(s)):
            if s[i] in lu_fwd and lu_fwd[s[i]] != t[i]:
                return False
            if t[i] in lu_back and s[i] != lu_back[t[i]]:
                return False
            lu_fwd[s[i]] = t[i]
            lu_back[t[i]] = s[i]
        return True


if __name__ == "__main__":
    sol = Solution()
    result = sol.isIsomorphic("baba", "bada")
    assert result == False
    result = sol.isIsomorphic("foo", "bar")
    assert result == False
    result = sol.isIsomorphic("fod", "baa")
    assert result == False
    result = sol.isIsomorphic("fod", "bat")
    assert result == True
