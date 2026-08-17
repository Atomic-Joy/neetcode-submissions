class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        s = f = d
        for _ in range(n):
            f = f.next
        while f.next:
            s, f = s.next, f.next
        s.next = s.next.next
        return d.next