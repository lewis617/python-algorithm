# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        ans = []
        def pathSum2(root, sumValue, path):
            if not root:
                return
            if not root.left and not root.right and root.val == sumValue:
                path.append(root.val)
                ans.append(path)
            if root.left:
                pathSum2(root.left, sumValue-root.val, path+[root.val])
            if root.right:
                pathSum2(root.right, sumValue-root.val, path+[root.val])
            
        pathSum2(A, B, [])
        return ans
