# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initiate an empty node
        head = ListNode()
        # Save the head as a new variable
        dummy = head

        # while either of the lists are valid
            # If val1 <= val2, connect node1 to the dummy and move it a step
            #Else, connect node2 to the dummy and move it a step
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        #If either of the lists have remaining elements, connect them
        if list1:
            head.next = list1
        else:
            head.next = list2

        #Return head
        return dummy.next