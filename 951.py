# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def compare(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                return False
            elif node1.val != node2.val:
                return False
            elif node1.val == node2.val:
                left = compare(node1.left, node2.left) and compare(node1.right, node2.right)
                right = compare(node1.left, node2.right) and compare(node1.right, node2.left)
                return left or right

        return compare(root1, root2)

