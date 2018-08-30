class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        ans = 0
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                ans += A[i] - A[i-1]
        return ans


s = Solution()
print(s.maxProfit([1, 3, 2, 4]))
