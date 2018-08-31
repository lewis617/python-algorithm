class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        dp = [0] * (A+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, A+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]