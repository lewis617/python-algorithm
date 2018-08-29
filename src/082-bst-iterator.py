# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.pushAllLeft(root)
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack
        

    # @return an integer, the next smallest number
    def next(self):
        n = self.stack.pop()
        self.pushAllLeft(n.right)
        return n.val
    
    def pushAllLeft(self, n):
        while n:
            self.stack.append(n)
            n = n.left
        
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n1.left = n2
n1.right = n5
n2.left = n3
n2.right = n4
n5.right = n6
# Your BSTIterator will be called like this:
i = BSTIterator(n1)
while i.hasNext(): print i.next(),
