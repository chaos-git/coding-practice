'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.min_stack = []
        self.stack_min(root)

    def stack_min(self, node):
        if node:
            self.min_stack.append(node)
            self.stack_min(node.left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.min_stack) > 0

    def next(self):
        """
        :rtype: int
        """
        return_node = self.min_stack.pop()

        if return_node.right:
            self.stack_min(return_node.right)

        return return_node.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
