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


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        a,b = self.splitList(A)
        return self.mergeList(a, self.reverseList(b))

    def splitList(self, A):
        fast = slow = A
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        return A, middle

    def reverseList(self, A):
        last = None
        current = A
        while current:
            nextNode = current.next
            current.next = last

            last = current
            current = nextNode
        return last

    def mergeList(self, A, B):
        p1 = A
        p2 = B
        while p2:
            p1Next = p1.next
            p2Next = p2.next

            p2.next = p1.next
            p1.next = p2

            p1 = p1Next
            p2 = p2Next

        return A


s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

n4 = ListNode(4)
n5 = ListNode(5)
n4.next = n5
n3.next = n4
# print(s.splitList(n1)[1].log())
# print(s.reverseList(n1).log())
# print(s.mergeList(n1, n4).log())
print(s.reorderList(n1).log())
