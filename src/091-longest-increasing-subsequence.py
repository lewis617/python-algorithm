class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        dp = [1] * len(A)
        for i in range(len(A)):
            for j in range(i):
                if A[j] < A[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()
print(s.lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
