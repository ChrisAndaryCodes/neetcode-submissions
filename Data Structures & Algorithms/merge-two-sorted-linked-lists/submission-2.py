# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Create a dummy node to start the merged list
        dummy = ListNode()

        # Tail points to the last node in our merged list
        tail = dummy

        # Continue while both lists still have nodes
        while list1 and list2:

            # Compare the current values of both lists
            if list1.val < list2.val:

                # Connect the smaller node to our merged list
                tail.next = list1

                # Move list1 to its next node
                list1 = list1.next

            else:
                # Connect the node from list2
                tail.next = list2

                # Move list2 to its next node
                list2 = list2.next

            # Move tail to the node we just connected
            tail = tail.next

        # Attach any remaining nodes from list1
        if list1:
            tail.next = list1

        # Otherwise, attach remaining nodes from list2
        elif list2:
            tail.next = list2

        # Return the merged list, skipping the dummy node
        return dummy.next
