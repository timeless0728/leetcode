# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res_list=[]
        min_num = None
        start = 0

        while lists != [[]] and lists!= []:
            if min_num==None or (lists[start]!= [] and min_num[1]>lists[start].val):
                min_num=[start,lists[start].val]
            if start == len(lists)-1:
                res_list.append(min_num[1])
                if lists[min_num[0]].next!=[]:
                    lists[min_num[0]] = lists[min_num[0]].next
                else:
                    lists.remove(lists(min_num[0]))
                start = 0
            else:
                start+=1
        return res_list

solution = Solution()
print solution.mergeKLists([[]])
