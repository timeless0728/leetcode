class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if nums[mid] > target and nums[start] <= target:
                    end = mid - 1
                else:
                    start = mid + 1
            if nums[mid] < nums[end]:
                if nums[mid] < target and nums[end] >= target:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


solu = Solution()
print solu.search([4, 5, 6, 7, 0, 1, 2, 3], 8)
