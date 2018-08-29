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
    def t2Sum(self, A, B):
        if not A:
            return 0
        queue = [A]
        s = set()
        for i in queue:
            if i.val in s:
                return 1
            s.add(B-i.val)
            if i.left:
                queue.append(i.left)
            if i.right:
                queue.append(i.right)
        return 0
        
