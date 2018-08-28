# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        def dfs(root):
            if not root:
                return None
            if root.val in (B, C):
                return root
            left = dfs(root.left)
            right = dfs(root.right)
            if left and right:
                return root
            elif left or right:
                return left or right
        def dfsFind(root, val):
            if not root:
                return False
            if root.val == val:
                return True
            findLeft = dfsFind(root.left, val)
            findRight = dfsFind(root.right, val)
            if findLeft or findRight:
                return True
            return False
        findB = dfsFind(A, B)
        findC = dfsFind(A, C)
        if not findB or not findC:
            return -1
        n = dfs(A)
        return n.val if n else -1

s = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
# n1.right = n3
print(s.lca(n1, 4, 1))