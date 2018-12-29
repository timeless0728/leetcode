class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        if length == 2:
            return nums[1] if nums[0] > nums[1] else nums[0]
        elif nums[length / 2] <= nums[0]:
                return self.findMin(nums[:length / 2 + 1])
        elif nums[length / 2] > nums[0]:
            if nums[length / 2] > nums[-1]:
                return self.findMin(nums[length / 2:])
            elif nums[length / 2] <= nums[-1]:
                return self.findMin(nums[:length / 2])


solu = Solution()
print solu.findMin([4,5,6,7,0,1,2])
