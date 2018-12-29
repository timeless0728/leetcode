class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = sorted(A)
        a.append(100000)
        countnum = 0
        needadd = 0

        for i in xrange(1, len(a)):
            if a[i] == a[i - 1]:
                countnum -= a[i]
                needadd += 1
            else:
                give = min(needadd, a[i] - a[i - 1] - 1)
                countnum += give * (give + 1) / 2 + give * a[i-1]
                needadd -= give
        return countnum


solu = Solution()
print solu.minIncrementForUnique([7, 2, 7, 2, 1, 4, 3, 1, 4, 8])
