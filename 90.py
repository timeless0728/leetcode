class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = [[]]
        for i in nums:
            new_res = []
            for j in res:
                if j+[i] in res or j+[i] in new_res:
                    continue
                else:
                    new_res.append(j+[i])
            res = res + new_res
        return res

solu = Solution()
print solu.subsetsWithDup([1,2,2])