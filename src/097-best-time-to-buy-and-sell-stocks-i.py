class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        minimun = float('inf')
        profit = 0
        for i in A:
            minimun = min(minimun, i)
            profit = max(profit, i-minimun)
        return profit
