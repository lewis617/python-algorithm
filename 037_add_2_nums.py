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
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        p1 = A
        p2 = B
        carry = 0
        ans = p3 = ListNode(0)
        while p1 or p2 or carry > 0:
            num = carry
            if p1:
                num += p1.val
            if p2:
                num += p2.val
            carry = num/10
            p3.next = ListNode(num % 10)
            p3 = p3.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        return ans.next


s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

n4 = ListNode(4)
n5 = ListNode(5)
n4.next = n5
print(s.addTwoNumbers(n1, n4).log())
