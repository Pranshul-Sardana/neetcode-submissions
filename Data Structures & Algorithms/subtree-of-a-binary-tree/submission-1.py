# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #If subRoot is empty, it is a sub tree
        if not subRoot:
            return True

        #If tree is empty, it is not sub tree
        if not root:
            return False

        #Check if trees are the same
        if self.isSameTree(root, subRoot):
            return True
    
        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot))

    #Create a function to check if the trees are the same
    def isSameTree(self, p, q):
        #If both are empty, it is same
        if not p and not q:
            return True

        #If only one empty, it is not the same
        if not p or not q:
            return False

        #If values not equal, return False
        if p.val != q.val:
            return False
        
        #If values are equal, check the rest of subtree
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
