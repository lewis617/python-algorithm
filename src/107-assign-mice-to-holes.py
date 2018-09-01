class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        ans = 0
        for i in range(len(A)):
            ans = max(ans, abs(A[i]-B[i]))
        return ans


s = Solution()
print(s.mice([-49, 58, 72, -78, 9, 65, -42, -3],
             [30, -13, -70, 58, -34, 79, -36, 27]))
