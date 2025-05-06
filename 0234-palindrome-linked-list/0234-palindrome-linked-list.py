# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        def reverse(head):
            prev = None
            current = head

            while current:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp

            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverse(slow)
        first_half = head

        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True