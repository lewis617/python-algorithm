class Solution:
    def uniquePaths(self, m, n):
        martix = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    martix[i][j] = 1
                else:
                    martix[i][j] = martix[i - 1][j] + martix[i][j - 1]
        return martix[m - 1][n - 1]


s = Solution()
print(s.uniquePaths(2,2))
print(s.uniquePaths(1,2))
