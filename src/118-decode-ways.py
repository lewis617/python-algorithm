class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        l = len(s)
        dp = [0] * l
        dp[0] = 1
        for i in range(1, l):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if '09' < s[i-1:i+1] < '27':
                dp[i] += (dp[i-2] if i > 1 else 1)
        return dp[l-1]


s = Solution()
print(s.numDecodings('1204'))
