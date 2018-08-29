# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if A and B:
            return int(A.val == B.val and self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right))
        else:
            return int(A is B)
        

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(1)
n5 = TreeNode(2)
n6 = TreeNode(3)

n1.left = n2
n1.right = n3
n4.left = n5
n4.right = n6

s= Solution()
print(s.isSameTree(n1, n4))