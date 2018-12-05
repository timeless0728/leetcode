# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res_list = []
        res = []
        if root is None or root.val > sum:
            return []
        if root.val == sum:
            return [[root.val]]
        else:
            self.plus(root, sum, res, res_list)
        return res_list

    def plus(self, root, left_sum, res, res_list):
        if root is None:
            return None
        res.append(root.val)
        left_sum -= root.val

        if root.left is None and root.right is None and left_sum == 0:
            print root.val,res,111
            res_list.append(res)
            return
        print res
        self.plus(root.left, left_sum, res, res_list)
        self.plus(root.right, left_sum, res, res_list)






a=TreeNode(5)
b=TreeNode(4)
c=TreeNode(8)
d=TreeNode(11)
e=TreeNode(13)
f=TreeNode(4)
g=TreeNode(7)
h=TreeNode(2)
i = TreeNode(5)
j = TreeNode(1)


a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
d.left = g
d.right = h
f.left = i
f.right = j

solu = Solution()
print solu.pathSum(a,22)
