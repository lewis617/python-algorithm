# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        stack = [A]
        outputStack = []
        while stack:
            p = stack.pop()
            outputStack.append(p.val)
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        outputStack.reverse()
        return outputStack

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

s= Solution()
print(s.postorderTraversal(n1))