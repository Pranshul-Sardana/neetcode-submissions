# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #BFS with previous max
        def BFS(root, max_val, ret):
            #If child of the leaf node reached, return 0
            if not root:
                return 0

            # Add to the result 1 if curr_val >= previous max, else add 0
            # get current max
            ret = 1 if root.val >= max_val else 0
            max_val = max(max_val, root.val)

            #Iterate (and add) with left and the right nodes
            ret += BFS(root.left, max_val, ret)
            ret += BFS(root.right, max_val, ret)

            #return result
            return ret

        
        #Return
        return BFS(root, root.val, 0)
