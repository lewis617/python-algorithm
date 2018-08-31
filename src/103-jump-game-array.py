class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        curMax = nextMax = i = 0
        while nextMax < len(A)-1:
            while i<=curMax:
                nextMax = max(nextMax, i+A[i])
                if nextMax >= len(A) -1:
                    return 1
                i+=1
            if curMax == nextMax:
                return -1
            curMax == nextMax
        return 1
