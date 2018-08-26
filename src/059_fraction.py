class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        sign = '-' if A * B < 0 else ''
        head, remainder = divmod(abs(A), abs(B))
        tail, seen = '', {}
        while remainder != 0:
            if remainder in seen:
                tail = tail[: seen[remainder]] + '(' + tail[seen[remainder]:] + ')'
                break
            seen[remainder] = len(tail)
            digit, remainder = divmod( remainder*10, abs(B) )
            tail+=str(digit)
        return sign + str(head) + (tail and '.' + tail)


s = Solution()
print(s.fractionToDecimal(-10, 3))
# print(s.fractionToDecimal(1, 2))
# print(s.fractionToDecimal(6, 3))
print(s.fractionToDecimal(87, 22))
