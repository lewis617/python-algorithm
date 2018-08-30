# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        inorderList = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorderList.append(root.val)
            inorder(root.right)
        inorder(A)
        return inorderList[B-1]
            
