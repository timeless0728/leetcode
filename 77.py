class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        import itertools
        for i in itertools.combinations([i+1 for i in range(n)],k):
            res.append(list(i))
        return res
solu = Solution()
print solu.combine(4,2)