class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        l = filter(lambda x: x, [i.strip() for i in A.split(' ')])
        l.reverse()
        return ' '.join(l)


s = Solution()
print(s.reverseWords('a b'))
print(s.reverseWords(' a  b '))
