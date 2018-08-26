class Solution(object):
    res = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.dfs(s, 0)

    def dfs(self, s, dep):
        if dep == 4:
            return
        if s == '' and dep < 4:
            return
        for i in range(3):
            x = s[0]
            y = s[1:]
            return [x]+self.dfs(y, dep+1)

solu = Solution()
print solu.restoreIpAddresses('25525511135')
