class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for i in range(n)] for j in range(n)]
        num = 0
        for i in range(n / 2):
            for j in range(i, n - i - 1):
                num += 1
                res[i][j] = num
            for j in range(i, n - i - 1):
                num += 1
                res[j][n - i - 1] = num
            for j in range(n - i - 1, i, -1):
                num += 1
                res[n - i - 1][j] = num
            for j in range(n - i - 1, i, -1):
                num += 1
                res[j][i] = num

        if n % 2 == 1:
            res[n / 2][n / 2] = pow(n, 2)
        return res


solu = Solution()
print solu.generateMatrix(3)

