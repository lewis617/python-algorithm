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
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        if not A or not A.next:
            return None
        step = 0
        fast = A
        slow = ListNode(0)
        slow.next = A
        delFirst = True
        while fast.next:
            fast = fast.next
            step += 1
            if step >= B:
                slow = slow.next
                delFirst = False
        if delFirst:
            A = A.next
        else:
            slow.next = slow.next.next
        return A


s = Solution()
ll1 = list2LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7])
print(s.removeNthFromEnd(ll1, 10).log())
