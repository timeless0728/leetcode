class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m+1):
            res[i][1] = 1
        for j in range(n+1):
            res[1][j] = 1

        def cur(m, n):
            if res[m][n] == 0:
                res[m][n] = cur(m - 1, n) + cur(m, n - 1)
            return res[m][n]
        return cur(m, n)



solu = Solution()
print solu.uniquePaths(5, 10)
