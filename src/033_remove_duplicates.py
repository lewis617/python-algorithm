class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        j = 0

        for i in range(1, len(A)):
            if A[i] != A[j]:
                j += 1
                A[j] = A[i]
        A = A[:j + 1]
        return j + 1


s = Solution()
# print(s.removeDuplicates([1, 1, 1, -2, -2, 3]))
print(s.removeDuplicates([1, -1, 1, -2, 3, -2]))
