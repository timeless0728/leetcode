class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        rightMost = 1
        for i in range(0, len(nums)):
            if i + 1 > rightMost:
                break
            rightMost = max(rightMost, nums[i] + i + 1)

        return rightMost >= len(nums)


solu = Solution()
print solu.canJump([0, 2, 3])
