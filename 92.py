# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        origin_head = head

        before_tail = None
        after_head = None
        current_stack = []
        count = 0
        while head:
            count +=1
            if count<m:
                if count+1 == m:
                    before_tail = head
            elif n >= count >= m:
                current_stack.append(head)
            if count == n:
                after_head=head.next
                break
            head = head.next

        if before_tail:
            new_head = origin_head
            while len(current_stack)>0:
                before_tail.next = current_stack[-1]
                before_tail = current_stack[-1]
                current_stack.pop(-1)
            before_tail.next = after_head
        else:
            new_head = current_stack[-1]
            while current_stack:
                before_tail = current_stack[-1]
                current_stack.pop(-1)
                if current_stack:
                    before_tail.next = current_stack[-1]
                else:
                    before_tail.next=None
            before_tail.next = after_head
        return new_head


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
res = solu.reverseBetween(a, 1, 4)
print res
while res:
    print res.val,
    res = res.next






