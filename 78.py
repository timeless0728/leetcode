class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        res = []
        length = len(nums)
        for i in range(length+1):
            for j in itertools.combinations(nums,i):
               res.append(list(j))
        return res

solu = Solution()
print solu.subsets([1,2,3])