class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        ans = []
        A.sort()

        def dfs(index, path):
            ans.append(path)
            for i in range(index, len(A)):
                if i > index and A[i] == A[i-1]:
                    continue
                dfs(i + 1, path + [A[i]])
        dfs(0, [])
        return ans


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
