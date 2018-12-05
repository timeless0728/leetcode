class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0 for i in range(n+1)]
        res[0] = 1
        res[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                res[i] += res[i-j]*res[j-1]
        return res[n]

solu = Solution()
print solu.numTrees(3)