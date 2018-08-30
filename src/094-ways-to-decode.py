class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        if not A:
            return 0
        dp = [0] * (len(A) + 1)
        dp[0] = 1
        dp[1] = 1 if A[0] != '0' else 0
        for i in range(2, len(A) + 1):
            one = int(A[i-1: i])
            two = int(A[i-2: i])
            if 1<=one<=9:
                dp[i] += dp[i-1]
            if 10<=two<=26:
                dp[i] += dp[i-2]
        return dp[-1]
            
s = Solution()
print(s.numDecodings('10'))