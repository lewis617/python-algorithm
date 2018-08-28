# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        if not A:
            return
        self.flatten(A.right)
        self.flatten(A.left)
        A.right = self.prev
        A.left = None
        self.prev = A
        return A
        

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n1.left = n2
n1.right = n5
n2.left = n3
n2.right = n4
n5.right = n6

s = Solution()
t = s.flatten(n1)
print(t)