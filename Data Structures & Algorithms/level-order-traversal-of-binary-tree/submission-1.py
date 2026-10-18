# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS with aggregating each layer

        #Handle empty tree
        if not root:
            return []

        #Initiate deque and ret
        q = deque([root])
        ret = []

        #Implement Bfs
        while q:
            temp = []

            for _ in range(len(q)):
                curr = q.popleft()
    
                if curr:
                    temp.append(curr.val)

                    q.append(curr.left)
                    q.append(curr.right)
            
            if len(temp) > 0:
                ret.append(temp)

        return ret



        