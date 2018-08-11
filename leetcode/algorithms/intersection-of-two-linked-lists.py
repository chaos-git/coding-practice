'''
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        count_a = self.get_length(headA)
        count_b = self.get_length(headB)

        current_a = headA
        current_b = headB

        intersecting_node = None
        while count_a or count_b:
            if count_a == count_b:
                if current_a.val == current_b.val:
                    intersecting_node = intersecting_node or current_a
                else:
                    intersecting_node = None
            if count_a >= count_b:
                current_a = current_a.next
                count_a -= 1
            elif count_a <= count_b:
                current_b = current_b.next
                count_b -= 1

        return intersecting_node

    def get_length(self, node):
        count = 0
        current = node
        while current:
            count += 1
            current = current.next
        return count
