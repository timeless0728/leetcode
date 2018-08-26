class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(nums) - 1
        return self.binary(nums, target, low, high)

    def binary(self, nums, target, low, high):
        if low > high:
            return False
        mid = (low + high) / 2
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid]:
            return self.binary(nums, target, low + 1, high)
        if nums[low] < nums[mid]:
            if nums[mid] > target >= nums[low]:
                return self.binary(nums, target, low, mid - 1)
            else:
                return self.binary(nums, target, mid + 1, high)
        if nums[low] > nums[mid]:
            if nums[mid] < target <= nums[high]:
                return self.binary(nums, target, mid + 1, high)
            else:
                return self.binary(nums, target, low, mid - 1)


solu = Solution()
print solu.search([1, 3, 5], 4)
