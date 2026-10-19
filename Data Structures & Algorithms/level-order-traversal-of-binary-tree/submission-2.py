# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS

        #Handle empty inputs
        if not root:
            return []
        
        #Initaite deque. Append the first element. Initite res list
        q = deque()
        q.append(root)
        res = []

        #Iterate: while q
        while q:
            #Initiate temp list
            temp = []
            #for the length of elements in deque
            repeats = len(q)
            for i in range(repeats):
                #popleft element and add to the temp list
                root = q.popleft()
                temp.append(root.val)
 
                #If children are not empty, add to the deque
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            
            #If the temp list is not empty, add to the res list
            if len(temp) > 0:
                res.append(temp)

        #Return the res list
        return res