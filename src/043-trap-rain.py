class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        l, r, leftMaxHeight, rightMaxHeight = 0, len(A) - 1, 0, 0
        ans = 0
        while l < r:
            # fill water from left
            if A[l] <= A[r]:
                if A[l] > leftMaxHeight:
                    leftMaxHeight = A[l]
                else:
                    ans += leftMaxHeight - A[l]
                l += 1
            else:
                if A[r] > rightMaxHeight:
                    rightMaxHeight = A[r]
                else:
                    ans += rightMaxHeight - A[r]
                r -= 1
        return ans


s = Solution()
print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
