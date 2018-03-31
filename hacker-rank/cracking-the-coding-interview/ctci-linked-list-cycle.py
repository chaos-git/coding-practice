"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(root):
    iteration = 0
    head = root
    tail = root
    while head.next:
        if head == tail and iteration != 0:
            return True
        if iteration % 2:
            tail = tail.next
        head = head.next
        iteration += 1
    return False