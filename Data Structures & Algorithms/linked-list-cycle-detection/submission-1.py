# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        #print(f'{curr = }')
        #print(f'{curr.next = }')
        #print(f'{curr.val = }')
        

        while curr:
            if curr.next in visited:
                return True
            else:
                visited.add(curr.next)

            curr = curr.next

        return False
