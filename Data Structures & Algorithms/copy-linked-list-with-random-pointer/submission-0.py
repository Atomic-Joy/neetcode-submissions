class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {None: None}
        c = head
        while c:
            m[c] = Node(c.val)
            c = c.next

        c = head
        while c:
            m[c].next = m[c.next]
            m[c].random = m[c.random]
            c = c.next

        return m[head]