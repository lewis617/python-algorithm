class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        dp1 = dp2 = 1
        for i in range(1, len(s)):
            dp3 = 0
            if s[i] != '0':
                dp3 += dp2
            if '09' < s[i-1:i+1] < '27':
                dp3 += dp1
            dp1, dp2 = dp2, dp3
        return dp2


s = Solution()
print(s.numDecodings('301'))
