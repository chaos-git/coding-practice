'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        evens = evens_tail = ListNode(None)
        odds = odds_tail = ListNode(None)

        is_odd = True
        current = head
        while current:
            if is_odd:
                odds_tail.next = current
                odds_tail = current
            else:
                evens_tail.next = current
                evens_tail = current
            is_odd = not is_odd
            current = current.next

        odds_tail.next = evens.next
        evens_tail.next = None
        return odds.next
