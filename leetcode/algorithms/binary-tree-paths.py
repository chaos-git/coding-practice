'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.list_paths('', root)

    def list_paths(self, prefix, root):
        if not root:
            return []
        new_prefix = prefix + ('->' if prefix else '') + str(root.val)
        if root.left or root.right:
            return self.list_paths(new_prefix, root.left) + self.list_paths(new_prefix, root.right)
        return [new_prefix]
