# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Initiate dummy
        dummy = ListNode(0, head)

        #Initiate 2 pointers
        left, right = dummy, head

        while right and n >0:
            right = right.next
            n -= 1

        #Move right pointer ahead and continue with regular iteration
        while right:
            left = left.next
            right = right.next

        #When right stops existing, skip the left
        left.next = left.next.next

        return dummy.next