# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is not None:
            self.parseLevel([root])

    def parseLevel(self, parselist):
        for i in range(len(parselist) - 1):
            parselist[i].next = parselist[i + 1]
        nextlist = []
        for i in range(len(parselist)):
            if parselist[i].left is not None:
                nextlist.append(parselist[i].left)
            if parselist[i].right is not None:
                nextlist.append(parselist[i].right)
        if len(nextlist) != 0:
            self.parseLevel(nextlist)