class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        ans = []
        def isPalindrome(s):
            s1 = s[::-1]
            return s1 == s

        def dfs(l, path):
            if l == len(A):
                ans.append(path)
                return
            for i in range(1, len(A) - l + 1):
                newStr = A[l:l+i]
                if(isPalindrome(newStr)):
                    dfs(i + l, path + [A[l:l+i]])
                
        dfs(0, [])
        return ans


s = Solution()
print(s.partition('aab'))
print(s.partition('a'))
print(s.partition(''))
