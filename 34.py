class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                low = high = mid
                while low > 0:
                    if nums[0] == target:
                        low = 0
                    elif nums[low] == nums[low - 1]:
                        low -= 1
                    else:
                        break
                while high < len(nums) - 1:
                    if nums[high] == nums[high + 1]:
                        high += 1
                    else:
                        break
                return [low, high]
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1

        return [-1, -1]


solu = Solution()
print solu.searchRange([1,2,3,3,5,7,8,8,9,10], 8)
