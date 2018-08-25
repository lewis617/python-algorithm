# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def log(self):
        l = []
        p = self
        l.append(p.val)
        while p.next:
            p = p.next
            l.append(p.val)
        print(l)


def list2LinkedList(l):
    ans = p = ListNode(l[0])
    for i in l[1:]:
        p.next = ListNode(i)
        p = p.next
    return ans


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        last = None
        current = fast = A
        while fast and fast.next:
            fast = fast.next.next
            last, last.next, current = current, last, current.next
        if fast:
            current = current.next
        while last and last.val == current.val:
            last, current = last.next, current.next
        return 1 if not last else 0


s = Solution()
l1 = list2LinkedList([1, 2, 3, 2, 1])
l2 = list2LinkedList([1, 2, 3, 2, 4])
l3 = list2LinkedList([1])
l4 = list2LinkedList([1, 1])
print(s.lPalin(l1))
print(s.lPalin(l2))
print(s.lPalin(l3))
print(s.lPalin(l4))
