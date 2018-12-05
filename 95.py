# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.makeatree(0, n)

    def makeatree(self, start, end):
        res_list = []
        if start == end-1:
            return [TreeNode(start+1)]
        elif start == end:
            return []
        for i in range(start, end):
            left_list = self.makeatree(start, i)
            right_list = self.makeatree(i+1, end)
            if not left_list:
                left_list = [None]
            if not right_list:
                right_list = [None]
            for left in range(len(left_list)):
                for right in range(len(right_list)):
                    node = TreeNode(i + 1)
                    node.left = left_list[left]
                    node.right = right_list[right]
                    res_list.append(node)
        return res_list

solu = Solution()
result = solu.generateTrees(3)
if [None]:
    print 'xxx'
print result
for i in result:
    print i.val
