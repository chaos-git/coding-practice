'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = next_node = None
        while l1 or l2:
            if not l1 or (l2 and l1.val >= l2.val):
                next_node = l2
                l2 = l2.next
            else:
                next_node = l1
                l1 = l1.next
            if not tail:
                head = tail = next_node
            else:
                tail.next = next_node
                tail = tail.next
        if tail:
            tail.next = None
        return head
