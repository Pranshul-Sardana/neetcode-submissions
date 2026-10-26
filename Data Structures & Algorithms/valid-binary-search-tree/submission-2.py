# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS

        def dfs(root, left, right):
            #Return True if end of the tree reached
            if not root:
                return True
            
            # Return False if condition of BST is invalid
            if root.val <= left or root.val >= right:
                return False

            return (dfs(root.left, left, root.val) and #Keep left boundary the same
                    dfs(root.right, root.val, right)) #Keep right boundary the same

            
        return dfs(root, float("-inf"), float("inf"))