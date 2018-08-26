class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                count = 1
                res += 1
            elif nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    continue
                else:
                    res += 1
        return res


solu = Solution()
print solu.removeDuplicates([0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 3])
