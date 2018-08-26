class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res_list = []
        res = []
        candidates.sort()
        self.dfs(candidates, target, res, res_list)
        return list(set([tuple(t) for t in res_list]))


    def dfs(self, candidates, target, res, res_list):
        if target == 0:
            print res_list
            res_list.append(list(res))
            return
        elif target < 0:
            return
        else:
            for i in range(len(candidates)):
                res.append(candidates[i])
                self.dfs(candidates[i+1:], target - candidates[i], res, res_list)
                res.pop()


solu = Solution()
print solu.combinationSum2([2, 5, 2, 1, 2], 5)
