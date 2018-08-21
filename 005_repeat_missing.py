class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        ans = [0, 0]
        tmp = [0] * len(A)
        for i in A:
            if tmp[i-1] == 0:
                tmp[i-1] = 1
            else:
                ans[0] = i
                tmp[i-1] = 1
        for i in range(len(tmp)):
            if tmp[i] == 0:
                ans[1] = i + 1
        return ans


s = Solution()
print(s.repeatedNumber([1, 2, 4, 4]))
print(s.repeatedNumber([3, 3, 1, 2]))
