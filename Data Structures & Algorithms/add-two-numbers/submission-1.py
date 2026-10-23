# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Add sequentially. Carry to the next
        # Save the new elements in new linked list

        #Initiate dummy node and carry
        dummy = ListNode()
        curr = dummy

        carry = 0

        #While either of the lists or carry has elements
        while l1 or l2 or carry:
            #Get the value from the node
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Add values and carry
            val = v1 + v2 + carry
            # Use val%10 as the current value
            curr.next = ListNode(val%10)
            
            # Carry val//10 to the next iteration
            carry = val//10

            # Move to the next nodes of the list and curr
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None


        #Return
        return dummy.next
