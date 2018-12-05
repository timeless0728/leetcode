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
        for i in range(len(parselist)-1):
            parselist[i].next = parselist[i+1]
        nextlist = []
        if parselist[0].left is not None:
            for i in range(len(parselist)):
                nextlist.append(parselist[i].left)
                nextlist.append(parselist[i].right)
            self.parseLevel(nextlist)

solu = Solution()
solu.connect(None)