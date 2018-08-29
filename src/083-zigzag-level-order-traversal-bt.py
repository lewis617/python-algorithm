# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        ans = []
        curStack = [A]
        nextStack = []
        ltr = True
        row = []
        while curStack:
            n = curStack.pop()
            row.append(n.val)
            if ltr:
                if n.left:
                    nextStack.append(n.left)
                if n.right:
                    nextStack.append(n.right)
            else:
                if n.right:
                    nextStack.append(n.right)
                if n.left:
                    nextStack.append(n.left)
            if not curStack:
                ans.append(row)
                row = []
                ltr = not ltr
                curStack, nextStack = nextStack, curStack
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(7)
root.left.right = TreeNode(6)
root.right.left = TreeNode(5)
root.right.right = TreeNode(4)

s= Solution()
print(s.zigzagLevelOrder(root))