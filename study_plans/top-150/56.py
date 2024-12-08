# 56. Merge Intervals

from collections import defaultdict
from typing import List
from icecream import ic


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # this will ensure that we can guarantee that the first value of
        # each <= to the next meaning we only need to check the max value of
        # each interval to see if it overlaps which is the case when
        # intv[j][0] <= intv[i][1]
        out: List[List[int]] = []
        intervals.sort(key=lambda i: i[0])
        if not intervals:
            return []
        prev = intervals[0]
        if len(intervals) == 1:
            return [prev]
        for next in intervals[1:]:
            if next[0] <= prev[1]:
                # overlap so merge them
                prev[1] = max(prev[1], next[1])
            else:
                # not overlapping so save prev to out and then assign to next
                out.append(prev)
                prev = next
        out.append(prev)
        return out

        # out: List[List[int]] = []
        # seen = []
        # # _intervals = intervals
        # # next_intervals = []
        # cur = None

        # def compare(a: list[int], b: list[int]):
        #     return not (b[0] > a[1] or a[0] > b[1])

        # def merge(a: list[int], b: list[int]):
        #     return [min(a[0], b[0]),
        #             max(a[1], b[1])]

        # for i in range(len(intervals)):
        #     # if cur:
        #     #     _intervals += [cur]
        #     if i in seen:
        #         continue
        #     cur = intervals[i]
        #     seen.append(i)

        #     for j in range(i+1, len(intervals)):
        #         if j in seen:
        #             continue
        #         # if (intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][0]) or (intervals[i][0] <= intervals[j][1] and intervals[i][1] >= intervals[j][1]):
        #         # if (cur[0] <= intervals[j][0] and cur[1] >= intervals[j][0]) or (cur[0] <= intervals[j][1] and cur[1] >= intervals[j][1]):
        #         if compare(a=cur, b=intervals[j]):
        #             cur = merge(a=cur, b=intervals[j])
        #             seen.append(j)
        #     merged = False
        #     for i, c in enumerate(out):
        #         if compare(a=c, b=cur):
        #             out[i] = merge(a=c, b=cur)
        #             merged = True
        #             break
        #     if not merged:
        #         out.append(cur)
        # return out


if __name__ == "__main__":
    sol = Solution()
    kwargs_list = [
        ({"intervals": [[1, 4], [0, 5]]},
         [[0, 5]]),
        ({"intervals": [[1, 3], [4, 5], [6, 8], [1, 10]]},
         [[1, 10]]),
        ({"intervals": [[1, 3], [2, 6], [8, 10], [15, 18]]},
         [[1, 6], [8, 10], [15, 18]]),
        ({"intervals": [[1, 3], [2, 6], [8, 10], [15, 18], [4, 7]]},
         [[1, 7], [8, 10], [15, 18]]),
        ({"intervals": [[1, 3], [8, 10]]},
         [[1, 3], [8, 10]]),
        ({"intervals": [[1, 3]]},
         [[1, 3]]),
        ({"intervals": []},
         []),
        ({"intervals": [[1, 1], [1, 3]]},
         [[1, 3]]),
    ]
    for kwargs, expected in kwargs_list:
        result = sol.merge(**kwargs)
        assert result == expected
