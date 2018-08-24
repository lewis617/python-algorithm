class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        j = 0
        for i in A:
            if i != B:
                A[j] = i
                j += 1
        A = A[:j]
        return j


s = Solution()

print(s.removeElement([1, -1, 2, 1], 1))
