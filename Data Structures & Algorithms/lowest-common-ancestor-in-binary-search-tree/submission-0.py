# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        print(p.val, q.val)
        self.res = root

        def dfs(node, p , q):
            #Find recursively
            if node.val > p.val and node.val > q.val and node.left:
                return dfs(node.left, p , q)
            elif node.val < p.val and node.val < q.val and node.right:
                return dfs(node.right, p , q)
            else:
                return node

        return dfs(root, p , q)