# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        ans = []
        stack = []
        p = A
        while len(stack) or p:
            if p:
                stack.append(p)
                p = p.left 
            else:
                n = stack.pop()
                ans.append(n.val)
                p = n.right
        return ans

s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3
print(s.inorderTraversal(n1))
