# Last updated: 5/6/2025, 7:20:12 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                pointer = head
                while slow != pointer:
                    slow = slow.next
                    pointer = pointer.next
                return pointer

        return None