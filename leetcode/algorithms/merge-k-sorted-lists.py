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
        queue = PriorityQueue()
        for linked_list in lists:
            while linked_list:
                if linked_list:
                    queue.put((linked_list.val, linked_list))
                    linked_list = linked_list.next

        head = None
        tail = None
        while not queue.empty():
            val, new_tail = queue.get()
            if head is None:
                head = new_tail
                tail = new_tail
            else:
                tail.next = new_tail
                tail = new_tail

        if tail:
            tail.next = None

        return head
