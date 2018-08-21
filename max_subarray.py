from sys import maxint


class Solution:
    def maxSubArray(self, A):
        maxsum = cursum = A[0]
        for a in A[1:]:
            cursum = max(cursum + a, a)
            maxsum = max(cursum, maxsum)
        return maxsum


s = Solution()

print(s.maxSubArray([-1, -2, 3, 4, -5, -4, 3, 1, 6]))
print(s.maxSubArray([-5, -3]))
print(s.maxSubArray([-3]))
