# 3 Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_str = ""
        for right in range(len(s)):
            if s[right] in cur_str:
                cur_str = cur_str[cur_str.index(s[right])+1:]
            cur_str += s[right]
            # print(cur_str)
            if len(cur_str) > max_len:
                max_len = len(cur_str)
        return max_len


if __name__ == "__main__":
    leet = 0
    sol = Solution()
    kwargs_list = [
        ({'s': "dvdf"}, 3),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.lengthOfLongestSubstring(**kwargs)
        assert expected == result
