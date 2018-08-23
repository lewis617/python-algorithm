class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        n = int(A)
        return 1 if n > 1 and not n & (n-1) else 0

s = Solution()
print(s.power(1))
print(s.power(2))