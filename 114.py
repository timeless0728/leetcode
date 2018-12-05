# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.merge(root)
    def merge(self,root):
        if root is None:
            return
        self.merge(root.right)
        self.merge(root.left)

        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(5)
d=TreeNode(3)
e=TreeNode(4)
f=TreeNode(6)



a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


solu = Solution()
res = solu.flatten(a)
while a:
    print a.val
    a = a.right