class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        for i in range(len(A)):
            if A[i] == '(':
                stack.append(i)
            if A[i] == ')':
                l = stack[-1]
                if '+' in A[l:i+1] or '-' in A[l:i+1] or '*' in A[l:i+1] or '/' in A[l:i+1]:
                    A = A[:l] + (i-l+1)*'a' + A[min(i+1, len(A)-1):]
                    stack.pop()
                else:
                    return 1
        return 1 if len(stack) else 0


s = Solution()
print(s.braces('((a+b))'))
print(s.braces('(a+(a+b))'))
print(s.braces('(a*b)+(b*c)'))
