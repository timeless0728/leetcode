# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        mid = self.get_mid(head)
        l = head
        r = mid.next
        mid.next = None
        return self.merge(self.sortList(l), self.sortList(r))

    def merge(self, p, q):
        tmp = ListNode(0)
        h = tmp
        while p and q:
            if p.val < q.val:
                h.next = p
                p = p.next
            else:
                h.next = q
                q = q.next
            h = h.next
        if p:
            h.next = p
        if q:
            h.next = q
        return tmp.next

    def get_mid(self, node):
        if node is None:
            return node
        fast = slow = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


solu = Solution()
a = ListNode(4)
b = ListNode(2)
c = ListNode(3)
d = ListNode(1)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
res = solu.sortList(a)
print res
while res:
    print 4,res.val,
    print
    res = res.next



