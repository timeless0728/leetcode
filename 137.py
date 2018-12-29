class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i = 0
        while i<len(nums):
            if i+2>len(nums):
                return nums[i]
            if nums[i] == nums[i+1] == nums[i+2]:
                i+=3
            else:
                return nums[i]^nums[i+1]^nums[i+2]

solu = Solution()
print solu.singleNumber([0,1,0,1,0,1,99])