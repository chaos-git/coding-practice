""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return checkBSTRecursive(root, None, None)

def checkBSTRecursive(root, minimum, maximum):
    if not root:
        return True
    if (minimum and minimum >= root.data) or (maximum and maximum <= root.data):
        return False
    return checkBSTRecursive(root.left, minimum, root.data) and checkBSTRecursive(root.right, root.data, maximum)