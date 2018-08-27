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
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        dummy = ListNode(0)
        dummy.next = A
        pre = dummy

        for _ in range(B-1):
            pre = pre.next
        last = None
        current = pre.next
        for _ in range(C-B+1):
            nextNode = current.next
            current.next = last

            last = current
            current = nextNode
        pre.next.next = current  # pre.next.next means end.next
        pre.next = last
        return dummy.next


s = Solution()
l1 = list2LinkedList([1, 2, 3, 4, 5])
print(s.reverseBetween(l1, 2, 4).log())
