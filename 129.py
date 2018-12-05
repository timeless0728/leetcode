# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.numParse(root, 0, 0)

    def numParse(self, root, num, sumnum):
        if root is None:
            return sumnum
        if root.left is None and root.right is None:
            newnum = num * 10 + root.val
            sumnum += newnum
        else:
            if root.left is not None:
                sumnum = self.numParse(root.left, num * 10 + root.val, sumnum)
            if root.right is not None:
                sumnum = self.numParse(root.right, num * 10 + root.val, sumnum)
        return sumnum

a = TreeNode(4)
b = TreeNode(9)
c=TreeNode(0)
d = TreeNode(5)
e = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
solu = Solution()
print solu.sumNumbers(None)