class Solution:
    def titleToNumber(self, A):
        ans = 0
        for e in A:
            ans = ans * 26 + ord(e) - ord('A') + 1
        return ans