
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        trans = [
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
        ]

        transpow = [
            [2, 1, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 2, 0, 1, 0, 0, 0, 1, 0, 0],
            [0, 0, 2, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 0, 2, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 3, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 3, 0, 1, 0],
            [1, 1, 0, 0, 0, 0, 0, 2, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 2, 0],
            [1, 0, 0, 1, 0, 0, 0, 1, 0, 2],

        ]

        start = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        def cheng(trans, start):
            reslist = []
            for i in trans:
                res = 0
                for j in range(len(i)):
                    res += start[j] * i[j]
                reslist.append(res)
            return reslist

        def multi(vec, mat):
            m = len(vec)
            res = [0 for i in range(m)]
            for i in range(m):
                for j in range(m):
                    res[i] += vec[j] * mat[j][i]
            return res

        N = N - 1
        while N:
            if N >= 1:
                # start = cheng(trans, start)
                start = multi(start, trans)
                start = [x % (10**9 + 7) for x in start]
                N -= 1
                # print start
        print start
        return sum(start) % (10**9 + 7)

solu = Solution()
print solu.knightDialer(1)
