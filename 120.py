class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if len(triangle[i]) == 1:
                    triangle[i][j] = triangle[i][j]
                else:
                    if j == 0:
                        triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                    elif j == len(triangle[i]) - 1:
                        triangle[i][j] = triangle[i - 1][-1] + triangle[i][j]
                    else:
                        triangle[i][j] = min(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]

        return min(triangle[-1])

solu = Solution()
print solu.minimumTotal([[2]])