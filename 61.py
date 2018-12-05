# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        first = head
        count = 1
        if not head:
            return None
        if k == 0:
            return head
        while first.next:
            count += 1
            first = first.next
        first.next = head
        point = head
        step = count - k % count
        while step > 1:
            point = point.next
            step -= 1
        next_point = point.next
        point.next = None
        return next_point


solu = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
res = solu.rotateRight(e, 1)
print res
while res:
    print res.val,
    res = res.next
