# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/?envType=study-plan-v2&envId=top-interview-150
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
        """
        q: deque[str] = deque()
        if not s:
            return True

        for c in s:
            if c in [')', ']', '}']:
                if not q:
                    return False
                last = q.pop()
                if last != "(" and c == ')':
                    return False
                elif last != "{" and c == '}':
                    return False
                elif last != "[" and c == ']':
                    return False
                else:
                    continue
            else:
                q.append(c)
        return not q


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        ({"s": "()"}, True),
        ({"s": "]"}, False),
        ({"s": r"({})"}, True),
        ({"s": r"({])"}, False),
        ({"s": r""}, True),
        ({"s": r"[](){}[({[]}){}]"}, True),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.isValid(**kwargs)
        assert result == expected
