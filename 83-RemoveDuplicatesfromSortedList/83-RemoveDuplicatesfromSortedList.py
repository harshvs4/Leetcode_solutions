# Last updated: 5/5/2025, 8:02:39 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head

        while dummy and dummy.next:
            if dummy.next and dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return head
