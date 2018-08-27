# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        ans = []
        for i in A:
            while i:
                ans.append(i.val)
                i = i.next
        ans.sort()
        p = head = ListNode(ans[0])
        for i in range(1, len(ans)):
            p.next = ListNode(ans[i])
            p = p.next
        return head
