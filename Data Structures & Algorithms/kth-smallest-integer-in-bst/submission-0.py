# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Initiate a stack and count for the smallest
        n = 0
        stack = []

        #Initiate cur
        cur = root

        #Iterate till cur and stack are non empty:
        while cur or stack:
            #Iterate till cur is non null
            while cur:
                # Add curr to stack
                stack.append(cur)
                # Go to left
                cur = cur.left
                #print(f"{cur = }")

            #print(f"1{cur = }")
            # Pop the most recent stacked value (Guaranteed to be the next largest)
            cur = stack.pop()

            # Increment n
            # If n reaches k, return value
            n += 1
            #print(f"{n}")
            if n == k:
                return cur.val

            # Move to right
            cur = cur.right