class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        k=k-1
        choice = [str(i + 1) for i in range(n)]
        return self.cur(choice, k, res)

    def cur(self, choice, k, res):
        import math
        if len(choice) == 1:
            res += choice[0]
            return res
        count = math.factorial(len(choice) - 1)
        num = int(math.floor(k / count))
        next_k = k % count
        res += choice[num]
        choice = choice[0:num] + choice[num + 1:len(choice)]
        return self.cur(choice, next_k, res)


solu = Solution()
print solu.getPermutation(4, 9)
