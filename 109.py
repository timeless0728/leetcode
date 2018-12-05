# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        start = head
        while start and start.next:
            start = start.next
        return self.cur(head, start)

    def cur(self, head, end):
        start = head
        second_point = head
        left_end = head
        count = 0
        if start is None:
            return None
        if start == end:
            return TreeNode(start.val)
        while start.next is not None and start != end:
            start = start.next
            if count % 2 == 0:
                if count >= 1:
                    left_end = second_point
                second_point = second_point.next

            count += 1
        root = TreeNode(second_point.val)
        if second_point!=left_end:
            root.left = self.cur(head, left_end)
        if second_point!=end:
            root.right = self.cur(second_point.next, end)
        return root


a = ListNode(-10)
b = ListNode(-3)
c = ListNode(0)
d = ListNode(5)
e = ListNode(9)
a.next = b
b.next = c
c.next = d
d.next = e
solu = Solution()
res = solu.sortedListToBST(a)
def printtree(res):
    print res.val
    if res.left:
        print res.val,'=>left',printtree(res.left)
    if res.right:
        print res.val,'=>right',printtree(res.right)
printtree(res)
