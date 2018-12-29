class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        else:
            flag_num = len(nums)
            for i in range(len(nums) - 1, 0, -1):
                if nums[i - 1] < nums[i]:
                    flag_num = i
                    break
            print flag_num
            if flag_num == 0:
                nums.reverse()
                return nums
            elif flag_num == len(nums) - 1:
                nums[-1], nums[-2] = nums[-2], nums[-1]
            else:
                for j in range(len(nums) - 1, flag_num - 1, -1):
                    if nums[j] > nums[flag_num - 1]:
                        print nums[j]
                        nums[j], nums[flag_num - 1] = nums[flag_num - 1], nums[j]
                        start = flag_num
                        end = len(nums) - 1
                        while start < end:
                            nums[start], nums[end] = nums[end], nums[start]
                            start += 1
                            end -= 1
                        break
            return nums


solu = Solution()
print solu.nextPermutation([1, 3, 2])
