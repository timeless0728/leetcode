# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        new_head = None
        new_tail = None
        old_head = None
        old_tail = None
        if not head:
            return head
        while head:
            if head.val >= x:
                if not old_head:
                    old_head = head
                    old_tail = head
                else:
                    old_tail.next = head
                    old_tail = head
            else:
                if not new_head:
                    new_head = head
                    new_tail = head
                else:
                    new_tail.next = head
                    new_tail = head
            head = head.next
        if old_tail:
            old_tail.next = None
        if new_tail:
            new_tail.next = old_head
            return new_head
        else:
            return old_head
import time
def test1():
    flag = None
    for i in range(1000000):
        if not flag:
            a = 1

def test2():
    flag = None
    for i in range(1000000):
        if flag is not None:
            a = 1
def test3():
    flag = 3
    for i in range(1000000):
        if flag >= 3:
            a = 1

def test4():
    flag = 3
    for i in range(1000000):
        if flag < 4:
            a = 1
t1 = time.time()
test1()
t2 = time.time()
print 'time for test1', t2 - t1
t1 = time.time()
test2()
t2 = time.time()
print 'time for test2', t2 - t1
t1 = time.time()
test3()
t2 = time.time()
print 'time for test3', t2 - t1
t1 = time.time()
test4()
t2 = time.time()
print 'time for test4', t2 - t1
solu = Solution()
a = ListNode(1)
b = ListNode(4)
c = ListNode(3)
d = ListNode(2)
e = ListNode(5)
f = ListNode(2)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
res = solu.partition(a, 3)
print res
while res:
    print res.val,
    res = res.next
