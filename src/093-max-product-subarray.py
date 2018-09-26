class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        maxium = big = small = A[0]
        for i in A[1:]:
            big, small = max(i, i*big, i*small), min(i, i*small, i*big)
            maxium = max(maxium, big)
        return maxium

s= Solution()
print(s.maxProduct([-2,0,-1, 2,3,4,-5,3,100,4]))