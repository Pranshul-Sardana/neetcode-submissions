# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Initiate dummy node
        dummy = ListNode()
        cur = dummy

        #Initaiate carry
        carry = 0

        #While either of the nodes or carry
        while l1 or l2 or carry:
            #Get the values
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #Sum
            temp = v1 + v2 + carry

            #Update node value
            cur.next = ListNode(temp%10)

            #Update carry
            carry = temp//10

            #Move to the next nodes
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        #Return
        return dummy.next