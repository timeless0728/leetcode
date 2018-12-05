# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        if fast is not None:
            fast = fast.next
        else:
            return None
        if fast is not None:
            fast = fast.next
        else:
            return None
        slow = slow.next
        while fast != slow:
            if fast is not None:
                print fast.val
                fast = fast.next
            else:
                return None
            if fast is not None:
                print fast.val
                fast = fast.next
            else:
                return None
            slow = slow.next
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow

solu = Solution()
a = ListNode(1)
print solu.detectCycle(a)