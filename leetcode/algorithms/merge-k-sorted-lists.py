'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heads = lists[:]
        result_head = ListNode(None)
        result_tail = result_head

        pqueue = PriorityQueue()
        for h_index in range(len(heads)):
            if heads[h_index]:
                pqueue.put((heads[h_index].val, h_index))

        while not pqueue.empty():
            h_index = pqueue.get()[1]
            result_tail.next = heads[h_index]
            result_tail = result_tail.next
            if heads[h_index].next:
                heads[h_index] = heads[h_index].next
                pqueue.put((heads[h_index].val, h_index))

        result_tail.next = None
        return result_head.next
