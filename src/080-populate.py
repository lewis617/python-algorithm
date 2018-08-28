# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, A):
        if not A:
            return
        A.next = None
        while A:
            B = A
            while B:
                if B.left:
                    if B.right:
                        B.left.next = B.right
                    else:
                        B.left.next = self.nextRight(B)
                if B.right:
                    B.right.next = self.nextRight(B)
                    
                B = B.next
            if (A.left):
                A = A.left
            elif (A.right):
                A = A.right
            else:
                A = self.nextRight(A)

    def nextRight(self, current):
        currNext = current.next
    
        while (currNext):
            if (currNext.left):
                return currNext.left
            elif (currNext.right):
                return currNext.right
            currNext = currNext.next
        return None

            
        
        
