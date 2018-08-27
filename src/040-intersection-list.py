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
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        if not A or not B:
            return None
        p1 = A
        p2 = B
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = B
            if p2:
                p2 = p2.next
            else:
                p2 = A
        return p1


s = Solution()
l1 = list2LinkedList([1, 2])
l2 = list2LinkedList([3, 4])
l3 = list2LinkedList([5, 6])
l1.next.next = l3
l2.next.next = l3
print(s.getIntersectionNode(l1, l2).val)
