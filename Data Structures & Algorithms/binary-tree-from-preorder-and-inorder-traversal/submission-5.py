# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order_hm = {v: i for i, v in enumerate(inorder)}
        pre_order_idx = [0]

        def helper(l, r):
            if l > r:
                return None
        
            # 0th element of the preorder list is node
            rootValue = preorder[pre_order_idx[0]]
            root = TreeNode(rootValue)
            
            #Increment preorder idx
            pre_order_idx[0] += 1
            
            #Inorder index
            inorder_index = in_order_hm[rootValue]

            # Left of the location is left subtree
            # Right of the location is right subtree
            root.left = helper(l, inorder_index-1)
            root.right = helper(inorder_index+1, r)

            return root

        return helper(0, len(preorder)-1)