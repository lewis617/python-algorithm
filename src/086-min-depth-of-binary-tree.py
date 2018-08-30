# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if not A: return 0
        d = self.minDepth(A.left), self.minDepth(A.right)
        return 1 + (min(d) or max(d))
