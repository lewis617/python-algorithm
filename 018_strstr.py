class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        for i in range(len(A) - len(B) + 1):
            if A[i: (len(B) + i)] == B:
                return i
        return -1


s = Solution()
print(s.strStr('12234', '34'))
print(s.strStr('1', '1'))
print(s.strStr('bbbbbbbbab', 'baba'))
