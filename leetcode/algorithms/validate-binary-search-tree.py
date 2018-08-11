'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid_bst(root, None, None)

    def is_valid_bst(self, node, left_limit, right_limit):
        if not node:
            return True
        if left_limit is not None and node.val <= left_limit:
            return False
        if right_limit is not None and node.val >= right_limit:
            return False

        left_valid = self.is_valid_bst(node.left, left_limit, node.val)
        right_valid = self.is_valid_bst(node.right, node.val, right_limit)

        return left_valid and right_valid
