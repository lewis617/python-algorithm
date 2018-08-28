# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, arr):
        if not arr:
            return None
 
        # find middle
        mid = (len(arr)) / 2
        
        # make the middle element the root
        root = TreeNode(arr[mid])
        
        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sortedArrayToBST(arr[:mid])
        
        # right subtree of root has all 
        # values >arr[mid]
        root.right = self.sortedArrayToBST(arr[mid+1:])
        return root