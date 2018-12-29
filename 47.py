class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        ans = []
        for i in itertools.permutations(nums):
            if list(i) not in ans:
                ans.append(list(i))
        return ans


solu = Solution()
print solu.permuteUnique([1,1,2])