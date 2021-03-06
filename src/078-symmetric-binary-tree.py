# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None:
          return 1
        else:
          return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if left is None and right is None:
          return 1
        if left is None or right is None:
          return 0
    
        if left.val == right.val:
          outPair = self.isMirror(left.left, right.right)
          inPiar = self.isMirror(left.right, right.left)
          return 1 if outPair and inPiar else 0
        else:
          return 0
