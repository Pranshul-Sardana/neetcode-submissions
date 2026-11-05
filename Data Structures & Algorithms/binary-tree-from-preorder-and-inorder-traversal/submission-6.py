# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # The first element of the preorder list is the node
        # It's location in the inorder list splits the tree
        # Make the search process cheaper [O(n) -> O(1)]
        inorder_dict = {val:index for index, val in enumerate(inorder)}
        preorder_index = [0]
        
        #Recurse
        def helper(l, r):
            #Use left and right pointers
            if l > r:
                return

            #Use the first element and put it on a tree node (root)
            root_val = preorder[preorder_index[0]]
            root = TreeNode(root_val)
            #Increment preorder index
            preorder_index[0] += 1
            
            #Search it's location in the inorder
            inorder_index = inorder_dict[root_val]

            #Create node left and node right
            root.left = helper(l,inorder_index-1)
            root.right = helper(inorder_index+1,r)

            #Return root
            return root

        #Return
        return helper(0, len(preorder)-1)

        