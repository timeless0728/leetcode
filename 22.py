def getstr(left, right, str, res):
    if not left and not right:
        res.append(str)
    if left > 0:
        getstr(left - 1, right, str + '(', res)
    if left < right:
        getstr(left, right - 1, str + ')', res)
    return res

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return getstr(n,n,'',[])


solution = Solution()
print solution.generateParenthesis(3)