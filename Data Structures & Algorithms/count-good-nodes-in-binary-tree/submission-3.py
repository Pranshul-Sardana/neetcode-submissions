# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #dfs
        def dfs(root, max_val, good):
            #If leaf node, return 0
            if not root:
                return 0

            #update good count
            good = 1 if root.val >= max_val else 0

            #Update max val
            max_val = max(max_val, root.val)

            #recurse left
            good += dfs(root.left, max_val, good)
            
            #recurse right
            good += dfs(root.right, max_val, good)
            
            #return good count
            return good

        #DFS with root, curr max, good count
        return dfs(root, root.val, 0)
