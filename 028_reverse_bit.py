class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        n = '{0:032b}'.format(A)
        return int(n[::-1], 2)

s = Solution()
print(s.reverse(0))
print(s.reverse(3))