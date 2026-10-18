# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        #LCA if one item is smaller (or equal) and the other item is larger (or equal)
        #If both items are smaller, search left
        #If both items are larger, search right
        
        while root:
            if p.val < root.val and q.val < root.val:
                 root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root