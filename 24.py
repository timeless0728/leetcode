# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        start = None
        tmp = None
        first = None
        second = None
        originhead = head
        while head:
            if count%3 == 0:
                second = head
                head = head.next
            elif count%3 == 1:
                first = head
            elif count%3 == 2:
                head = head.next
                if start:
                    second, first = first, second
                    first.next = second.next
                    second.next = first
                    tmp.next = second
                    tmp = first
                else:
                    start = first
                    second, first = first, second
                    first.next = second.next
                    second.next = first
                    tmp = first
            count += 1
        if not start:
            start = originhead
        return start


solu = Solution()
a = ListNode(2)
b = ListNode(5)
c = ListNode(3)
d = ListNode(4)
e = ListNode(6)
f = ListNode(2)
g = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
res = solu.swapPairs(a)
print res
while res:
    print res.val
    res = res.next
