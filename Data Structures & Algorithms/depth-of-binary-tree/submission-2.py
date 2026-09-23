# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#-----------------BFS--------------------#

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Handle empty root
        if not root:
            return 0

        #Initiate a deque and add the first element
        dq = deque([root])
        
        #Initate depth
        depth = 0

        #Loop till the deque is empty
        while dq:
            
            for _ in range(len(dq)):
                #Pop the first (LEFT) element
                node = dq.popleft()

                # Add the children
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            depth += 1
            
        return depth