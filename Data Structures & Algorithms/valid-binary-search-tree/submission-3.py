# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # DFS with range
        def DFS(root, left, right):
            # If child of leaf, return True
            if not root:
                return True
            
            # If the curr val outside the range, return False
            if not (left < root.val < right):
                return False

            # Recurse with left and right
            return (DFS(root.left, left, root.val) and
                    DFS(root.right, root.val, right)
                    )

        #Return
        return DFS(root, -math.inf, math.inf)