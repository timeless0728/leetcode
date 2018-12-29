class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        if len(nums)==1 or nums[0] != nums[1]: return nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i] != nums[i-1] and nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

solu = Solution()
print solu.singleNumber([1,0,1])