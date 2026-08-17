class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None
        while slow.next:
            slow.next, prev, slow = prev, slow, slow.next
        slow.next = prev

        first, second = head, slow
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next