class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        ans = []

        def dfs(path):
            l = len(path)
            if l == B:
                ans.append(path)
                return
            for i in range(path[-1]+1 if len(path) else 1, A + 1):
                dfs(path + [i])
        dfs([])
        return ans


s = Solution()
print(s.combine(4, 2))
print(s.combine(1, 1))
print(s.combine(4, 1))
