# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head
        second = None
        before = None
        while first.next:
            if n > 2:
                n -= 1
            elif n <= 2:
                if n <= 1:
                    if not before:
                        before = head
                    else:
                        before = before.next
                if not second:
                    second = head
                else:
                    second = second.next
                n -= 1
            first = first.next
        if before:
            before.next = before.next.next
            return head
        elif second:
            return second.next
        else:
            return None



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
res = solu.removeNthFromEnd(a, 1)
print res.val
while res and res.next:
    print res.val,
    res = res.next