# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def recu(root):
            if root is not None:
                res.append(root.val)
                recu(root.left)
                recu(root.right)
        recu(root)
        return res