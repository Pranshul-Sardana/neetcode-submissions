# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#-----------------DFS--------------------#

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #Initiate stack and depth
        stack = [[root, 1]]
        depth = 0
        
        #While elements in the stack
        while stack:
            #Take the top element
            node, level = stack.pop()

            #Update depth and add children
            if node:
                depth = max(depth, level)

                stack.append([node.left, 1 + level])
                stack.append([node.right, 1 + level])

        #return depth
        return depth