# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Handle empty root
        if not root:
            return 0

        #Initiate stack
        stack = [[root,1]]
        d = 0

        #Iteratively go through the stack and update the stack and depth
        while stack:
            node, level = stack.pop()

            if node:
                stack.append([node.left, level+1])
                stack.append([node.right, level+1])
                d = max(d, level)

        return d
