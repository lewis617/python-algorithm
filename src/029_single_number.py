class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        res = 0
        for i in A:
            res ^= i
        return res


s = Solution()
print(s.singleNumber([1, 2, 3, 2, 1]))
