class Solution:
    def numberToTitle(self, A):
        ans = ''
        while(A):
            ans = chr((A-1) % 26+65) + ans
            A = (A-1) / 26
        return ans


s = Solution()
print(s.numberToTitle(1))
print(s.numberToTitle(27))
