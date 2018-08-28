# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        def buildTree2(start, end):
            if start >= end:
                return
            maxVal = float('-inf')
            maxIndex = 0
            for i in range(start, end):
                if maxVal < A[i]:
                    maxVal = A[i]
                    maxIndex = i
            n = TreeNode(maxVal)
            n.left = buildTree2(start, maxIndex)
            n.right = buildTree2(maxIndex+1, end)
            return n
        return buildTree2(0, len(A))

s = Solution()
t = s.buildTree([1,2,3])
print(t)
