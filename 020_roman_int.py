class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def romanToInt(self, s):
        d = {
            'M': 1000,
            'C': 100,
            'D': 500,
            'X': 10,
            'L': 50,
            'I': 1,
            'V': 5
        }
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res


s = Solution()
print(s.romanToInt('I'))
print(s.romanToInt('IV'))
print(s.romanToInt('C'))
