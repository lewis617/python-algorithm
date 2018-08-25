class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        obj = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack=[]
        for i in A:
            if i in obj:
                stack.append(i)
            elif len(stack) > 0 and i == obj[stack[-1]]:
                stack.pop()
            else:
                return 0
        return 1 if len(stack) == 0 else 0


s = Solution()
print(s.isValid('()[]{}'))
print(s.isValid('(({[]()}))'))
print(s.isValid('([)]'))
print(s.isValid(')]'))
