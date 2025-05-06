# Last updated: 5/7/2025, 7:12:45 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(head):
            prev = None
            current = head

            while current:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp

            return prev

        second = reverse(slow.next)
        slow.next = None

        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        