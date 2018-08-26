class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(length - i - 1):
                matrix[i][j], matrix[length - j - 1][length - i - 1] = matrix[length - j - 1][length - i - 1], \
                                                                       matrix[i][j]

        matrix.reverse()


solu = Solution()
print solu.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
