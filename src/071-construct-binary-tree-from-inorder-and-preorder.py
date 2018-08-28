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
        root = TreeNode(A[0])
        # find index of root of inorder list
        rootIndex = 0
        for i in range(len(B)):
            if B[i] == A[0]:
                rootIndex = i
                break
        root.left = self.buildTree(A[1:1+rootIndex], B[:rootIndex])
        root.right = self.buildTree(A[1+rootIndex:], B[rootIndex+1:])
        return root


s = Solution()
t = s.buildTree([1, 2, 3, 4, 5], [3, 2, 4, 1, 5])
print(t)
