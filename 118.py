class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1,numRows+1):
            item = []
            if i == 1:
                item.append(1)
            else:
                for j in range(i):
                    if j==0 or j==i-1:
                        item.append(1)
                    else:
                        item.append(res[-1][j-1]+res[-1][j])
            res.append(item)
        return res
solu = Solution()
print solu.generate()