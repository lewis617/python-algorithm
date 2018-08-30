class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) <= 1:
            return 0
        left = [0] * len(A)
        minimun = A[0]
        for i in range(1, len(A)):
            minimun = min(minimun, A[i])
            left[i] = max(left[i-1], A[i] - minimun)

        right = [0] * len(A)
        maximum = A[-1]
        for i in range(len(A)-2, -1, -1):
            maximum = max(A[i], maximum)
            right[i] = max(right[i+1], maximum - A[i])
        profit = 0
        for i in range(len(A)):
            profit = max(left[i] + right[i], profit)
        return profit

s = Solution()
p = s.maxProfit((1, 2, 1, 2, 1, 4, 3, 5))
print(p)
