# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.getRoot(preorder,inorder)

    def getRoot(self, preorder, inorder):
        if preorder == [] or inorder == []:
            return None
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                inorder_lefthand = inorder[0:i]
                inorder_righthand = inorder[i + 1:len(inorder)] if i + 1 <= len(inorder) else []
                preorder_lefthand = preorder[1:len(inorder_lefthand) + 1]
                preorder_righthand = preorder[len(inorder_lefthand)+1:len(preorder)]

                root.left = self.getRoot(preorder_lefthand, inorder_lefthand)
                root.right = self.getRoot(preorder_righthand, inorder_righthand)

                return root

solu = Solution()
print solu.buildTree([3,9,20,15,7],[9,3,15,20,7]).val

x = [1,2,3]
print x[1:1]