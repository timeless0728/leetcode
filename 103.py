# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is not None:
            self.diptree([root], res)
        return res


    def diptree(self, root_list, res):
        child_list = []
        current_result = []
        for i in root_list:
            if i.left is not None:
                child_list.append(i.left)
            if i.right is not None:
                child_list.append(i.right)
            current_result.append(i.val)
        if len(res)%2 == 1:
            current_result.reverse()
        res.append(current_result)
        if child_list:
            self.diptree(child_list, res)


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right =e

solu = Solution()
res = solu.zigzagLevelOrder(a)
print res