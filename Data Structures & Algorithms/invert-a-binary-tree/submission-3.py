# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Handle empty nodes/roots
        if not root:
            return None

        #Invert elements of the current node
        temp = root.left
        root.left = root.right
        root.right = temp

        #Recursive
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root