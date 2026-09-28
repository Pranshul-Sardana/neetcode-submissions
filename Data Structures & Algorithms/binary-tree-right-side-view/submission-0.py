# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Handle edge case
        if not root:
            return []

        #BFS using deque
        q = deque([root])
        res = []

        while q:
            temp_list = []
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    temp_list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
                
            #Use the right most element of deque
            if temp_list:
                res.append(temp_list[-1])

        return res