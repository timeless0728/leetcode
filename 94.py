# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.inorder(root,result)
        return result

    def inorder(self, root, result):
        if root == None:
            return
        else:
            self.inorder(root.left, result)
            result.append(root.val)
            self.inorder(root.right,result)


sulu = Solution()
a = TreeNode(3)
b = TreeNode(2)
c = TreeNode(1)
c.right = b
b.left = a
print sulu.inorderTraversal(c)