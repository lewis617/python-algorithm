# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = -float('inf')
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        def dfs(root):
            if not root:
                return 0
            l = max(0, dfs(root.left))
            r = max(0, dfs(root.right))
            self.ans = max(self.ans, root.val+l+r)
            return max(l,r)+root.val
        dfs(A)
        return self.ans

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
s= Solution()
print(s.maxPathSum(n1))