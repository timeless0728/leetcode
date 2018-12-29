import numpy as np
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        trans = np.array([
             [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
             [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
        ], dtype=np.clongfloat)
        trans_pow = np.linalg.matrix_power(trans, N-1)
        res = np.ones(10).dot(trans_pow)
        print int(np.sum(res))
        return int(np.sum(res) % (10**9 + 7))

solu = Solution()
print solu.knightDialer(161)
