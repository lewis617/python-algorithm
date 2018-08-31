class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A < 1:
            return 0
        if A == 1:
            return 1
        if A ==2:
            return 2
        pre1 = 2
        pre2 = 1
        cur = 3
        for _ in range(2, A):
            cur = pre1 + pre2
            pre2 = pre1
            pre1 = cur
        return cur
            