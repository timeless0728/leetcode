class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        result = []
        self.cur(result,nums,[])
        return result


    def cur(self, res, nums, path):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.cur(res,nums,path)
            path.pop()
