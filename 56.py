# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []

        def f_cmp(x):
            return x.start

        intervals = sorted(intervals, key=f_cmp)

        comp = intervals[0]
        for i in range(len(intervals) - 1):
            if intervals[i].end >= intervals[i + 1].start:
                intervals[i + 1] = intervals[i] = Interval(min(intervals[i].start, intervals[i + 1].start),
                                                           max(intervals[i].end, intervals[i + 1].end))

        intervals = list(set(intervals))
        for i in intervals:
            print i.start, i.end
        return intervals


solu = Solution()
print solu.merge([Interval(1,4), Interval(2, 3)])
print solu.merge([Interval(1, 3), Interval(2, 6), Interval(8, 13), Interval(15, 23)])
