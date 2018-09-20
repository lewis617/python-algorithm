class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        dp = range(-1, len(s))
        for i in range(len(s)):
            r1=r2=0
            while i-r1>=0 and i+r1<len(s) and s[i-r1] == s[i+r1]:
                dp[i+r1+1] = min(dp[i+r1+1], dp[i-r1]+1)
                r1+=1
            while i-r2>=0 and i+r2+1<len(s) and s[i-r2] == s[i+r2+1]:
                dp[i+r2+2] = min(dp[i+r2+2], dp[i-r2]+1)
                r2+=1
        return dp[-1]
        
        
        
        
                
s = Solution()
print(s.minCut('fdafdsagfdagffadsafsd'))