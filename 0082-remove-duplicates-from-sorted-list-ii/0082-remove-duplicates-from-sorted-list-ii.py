# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = head
        prev = dummy

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current.next = current.next.next
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next

        return dummy.next
            