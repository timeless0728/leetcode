class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        f = s = 0
        for i in range(len(nums)):
            print nums
            tmp = nums[i]
            nums[i] = 2
            if tmp < 2:
                nums[f] = 1
                f += 1
            if tmp < 1:
                nums[s] = 0
                s += 1
        print nums


solu = Solution()
print solu.sortColors([2, 1, 2, 0, 1, 0, 2, 1, 1, 0])
