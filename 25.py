# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next
def reverse_node(start,k):
    """
    :param start:
    :param k:
    :return:startnode
    """
    node_list = []
    startNode = start
    next_node=None
    for i in range(k):
        node_list.append(startNode)
        if startNode and i!=k-1:
            startNode = startNode.next
        elif startNode and i==k-1:
            next_node = startNode.next
        elif not startNode or startNode.next:
            next_node =None
            return start
        else:
            return start
    for i in range(k-1, -1, -1):
        if i == 0:
            node_list[0].next = reverse_node(next_node,k)
            return node_list[k - 1]
        node_list[i].next = node_list[i - 1]
    return node_list[0]


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        return reverse_node(head,k)

solu = Solution()
print solu.reverseKGroup([]
,1)




ListNode(1,ListNode(2,ListNode(3,ListNode(4))))


