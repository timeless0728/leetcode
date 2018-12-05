# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.getRoot(postorder,inorder)
    def getRoot(self, postorder, inorder):
        if postorder == [] or inorder == []:
            return None
        root = TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                inorder_lefthand = inorder[0:i]
                inorder_righthand = inorder[i + 1:len(inorder)] if i + 1 <= len(inorder) else []
                postorder_lefthand = postorder[0:i]
                postorder_righthand = postorder[i:len(postorder)-1]

                root.left = self.getRoot(postorder_lefthand, inorder_lefthand)
                root.right = self.getRoot(postorder_righthand, inorder_righthand)

                return root

solu = Solution()
print solu.buildTree([9,3,15,20,7],[9,15,7,20,3]).val
