# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if not len(A):
            return None
        root = TreeNode(B[-1])
        # find index of root of inorder list
        rootIndex = 0
        for i in range(len(A)):
            if A[i] == B[-1]:
                rootIndex = i
                break
        root.left = self.buildTree(A[:rootIndex], B[:rootIndex])
        root.right = self.buildTree(A[1+rootIndex:], B[rootIndex:-1])
        return root


s = Solution()
t = s.buildTree([2, 1, 3], [2, 3, 1])
print(t)
