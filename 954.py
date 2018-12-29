class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        res = sorted(A, key=abs)
        dic = {}
        for i in res:
            if dic.has_key(i):
                dic[i] += 1
            else:
                dic[i] = 1
        print res
        print dic

        for i in res:
            d = i * 2
            print d
            print dic
            if i in dic and dic[i] == 0:
                continue
            if d not in dic or dic[d] == 0:
                return False
            else:
                dic[i] -= 1
                dic[d] -= 1
                continue
        return True


solu = Solution()

print solu.canReorderDoubled([3,1,3,6])
