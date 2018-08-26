class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        ans = []
        A.sort()

        def dfs(index, path):
            ans.append(path)
            for i in range(index, len(A)):
                dfs(i + 1, path + [A[i]])
        dfs(0, [])
        return ans


s = Solution()
print(s.subsets([1, 2, 3]))
