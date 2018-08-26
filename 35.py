class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0
        return self.getIndex(nums, target, low, high)

    def getIndex(self, nums, target, low, high):
        mid = (low + high) / 2
        if low > high:
            return low
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            return self.getIndex(nums, target, mid + 1, high)
        if nums[mid] > target:
            return self.getIndex(nums, target, low, mid - 1)


solu = Solution()
print solu.searchInsert([1, 2, 3, 5, 6, 7, 8, 9], 4)
