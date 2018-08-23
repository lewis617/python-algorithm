class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        ans = 0
        for i in A[::-1]:
            if(ans == 0 and i == ' '):
                continue
            else:
                if(i == ' '):
                    return ans
                ans += 1
        return ans

s = Solution()
print(s.lengthOfLastWord('d'))
print(s.lengthOfLastWord('hello world '))
