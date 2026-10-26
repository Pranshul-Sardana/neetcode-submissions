# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Attempt with DFS

        #Initiate global good count
        gg = 0
        
        #DFS
        # Return None if None (child of a leaf node)
        # Have a previous max
        # If the current node val > previous max, increment global count and previous max
        # Recursive left
        # Recursive right
        def dfs(node, max_val):
            nonlocal gg
            if not node:
                return

            if node.val >= max_val:
                gg += 1
                max_val = node.val

            dfs(node.left, max_val)
            dfs(node.right, max_val)
            
        
        # Call DFS
        dfs(root, -101)

        #Return global good
        return gg
