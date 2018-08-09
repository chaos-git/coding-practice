'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        (max_length, max_diam) = self.track_max(root)
        return max_diam

    def track_max(self, node):
        if not node:
            return (0, 0)

        (left_depth, left_diam) = self.track_max(node.left)
        (right_depth, right_diam) = self.track_max(node.right)

        node_diam = left_depth + right_depth
        max_diam = max(node_diam, left_diam, right_diam)
        max_length = max(left_depth, right_depth)

        return (max_length + 1, max_diam)
