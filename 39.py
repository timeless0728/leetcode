class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        res_list = []
        self.dfs(candidates, target, res, res_list)
        return res_list

    def dfs(self, candidates, remain, res, res_list):
        if remain == 0:
            res_list.append(list(res))
        elif remain < 0:
            return
        else:
            for i in range(len(candidates)):
                res.append(candidates[i])
                self.dfs(candidates[i:], remain-candidates[i], res,  res_list)
                res.pop()

solu = Solution()
print solu.combinationSum([2,3,6,7], 7)