# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def cur(root):
            if root is None:
                return 0
            if R >= root.val >= L:
                res1 = cur(root.left)
                res2 = cur(root.right)
                return res1+res2+root.val
            elif root.val < L:
                return cur(root.right)
            elif root.val > R:
                return cur(root.left)

        return cur(root)


a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(15)
d = TreeNode(3)
e = TreeNode(7)
f = TreeNode(18)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

solu = Solution()
print solu.rangeSumBST(a, 7, 15)
