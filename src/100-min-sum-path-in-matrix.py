class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        m = len(A)
        n = len(A[0])
        for i in range(1, m):
            A[i][0] += A[i-1][0]
        for i in range(1, n):
            A[0][i] += A[0][i-1]
        for i in range(1, m):
            for j in range(1, n):
                A[i][j] += min(A[i-1][j], A[i][j-1])
        return A[-1][-1]


s = Solution()
print(s.minPathSum([[1, 3],
                    [4, 3],
                    [5, 6]
                    ]))
