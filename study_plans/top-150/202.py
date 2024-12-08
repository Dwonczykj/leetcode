from icecream import ic
# 202. Happy Number
# Favourite Solution: https://leetcode.com/problems/happy-number/solutions/5732946/video-2-solutions-using-remainder-and-two-pointers


class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            sq_digit_output = 0
            while n:
                right_most_digit = n % 10
                sq_digit_output += right_most_digit ** 2
                n = n // 10  # remove the right most digit
            if sq_digit_output == 1:
                return True
            else:
                n = sq_digit_output
        return False


if __name__ == "__main__":
    sol = Solution()
    result = sol.isHappy(19)
    assert result
