# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if not A or not A.next:
            return A
        p1 = p2 = p3 = A
        l = 1
        while p3.next:
            p3 = p3.next
            l += 1
        times = B % l
        if times == 0:
            return A
        for _ in range(times):
            p1 = p1.next
        while p1.next:
            p2 = p2.next
            p1 = p1.next
        temp = p2.next
        p1.next = A
        p2.next = None
        return temp


s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
h = n1
n1.next = n2
n2.next = n3
print(s.rotateRight(h, 9).val)
