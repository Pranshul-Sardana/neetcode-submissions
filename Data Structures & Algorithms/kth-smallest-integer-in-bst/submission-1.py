# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Keep a stack
        stack = []

        # Initate a pop count
        n = 0

        # While stack or root exists
        while stack or root:
            # While root exists
            while root:
                # append current node
                # Go left
                stack.append(root)
                root = root.left
            
            # Pop and update current
            root = stack.pop()

            # Increment pop count
            # If pop count reaches k, return
            n += 1
            if n == k: 
                return root.val

            # Go right of the root
            root = root.right
