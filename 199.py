# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        res = [root]
        while res:
            new_res = []
            for i in range(len(res)):
                if res[i].left:
                    new_res.append(res[i].left)
                if res[i].right:
                    new_res.append(res[i].right)
            result.append(res[-1].val)
            res = new_res

        return result
