class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    res.append([i,j])
        for z in res:
            i,j = z[0],z[1]
            matrix[i] = [0 for a in range(len(matrix[0]))]
            for i in range(len(matrix)):
                matrix[i][j] = 0
        print matrix
solu = Solution()
print solu.setZeroes([
    [0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]
])
