# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # 1 -> 2 -> 3 -> 4 -> 5
        while curr:
            temp = curr.next # Save the next Node
            curr.next = prev # Reverse the pointer
            prev = curr # Move previous to current
            curr = temp # Move current to the saved next Node
        return prev # Return the prev Node


        # Complexity
        # Time: O(n)
        # Space: O(1)