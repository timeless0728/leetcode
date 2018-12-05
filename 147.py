# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        sorted_head = ListNode(-1)
        while head:
            temp = head.next
            cur = sorted_head
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            head.next = cur.next
            cur.next = head

            head = temp
        return sorted_head.next


def printf(head):
    while head:
        print head.val
        head = head.next

solu = Solution()
a = ListNode(1)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)


a.next = b
b.next = d
d.next = c
print printf(solu.insertionSortList(a))

