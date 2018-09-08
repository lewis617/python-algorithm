class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        l = len(n)
        candidates = [str(pow(10, l)+1), str(pow(10, l-1)-1)]
        prefix = n[:(l+1)/2]
        prefixInt = int(prefix)
        for num in (prefixInt-1,prefixInt, prefixInt+1):
            if num == 0:
                continue
            p = str(num)
            s = p + (p[:-1] if l%2 else p)[::-1]
            candidates.append(s)
        def diff(x):
            return abs(int(n) - int(x))
        ans = None
        for c in candidates:
            if not ans or 0< diff(c) < diff(ans) or (diff(c) == diff(ans) and int(c) < int(ans)):
                ans = c
        return ans
        
s= Solution()
print(s.nearestPalindromic('100'))