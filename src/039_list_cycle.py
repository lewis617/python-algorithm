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
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        fast = slow = A
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                fast = A
                while(fast != slow):
                    fast = fast.next
                    slow = slow.next
                return fast
        
        return None



s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2
print(s.detectCycle(n1).val)
print(s.detectCycle(list2LinkedList([1,2,3])))
