class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        ans = []
        stack = []
        for i in A:
            while len(stack) and stack[-1] >= i:
                stack.pop()
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(i)
            
        return ans


s = Solution()
print(s.prevSmaller([4, 5, 2, 10, 8]))
print(s.prevSmaller([3, 2, 1]))
