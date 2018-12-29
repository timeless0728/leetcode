class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                return i - 1
        if len(nums) == 1:
            return 0
        else:
            return len(nums)-1