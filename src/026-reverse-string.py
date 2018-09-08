class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, s):
        l = s.strip().split()
        l.reverse()
        return ' '.join(l)


s = Solution()
print(s.reverseWords('a b'))
print(s.reverseWords(' a  b '))
