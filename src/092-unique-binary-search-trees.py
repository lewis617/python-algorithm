# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode 
    def generateTrees(self, A):
        def dfs(start, end):
            ans = []
            if start == end:
                return None
            for i in range(start, end):
                for l in dfs(start, i) or [None]:
                    for r in dfs(i+1, end) or [None]:
                        n = TreeNode(i)
                        n.left, n.right = l, r
                        ans.append(n)
            return ans
        return dfs(1, A+1)
