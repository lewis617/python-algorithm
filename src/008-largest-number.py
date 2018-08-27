class Solution:
    def largestNumber(self, nums):
        return ''.join(sorted(map(str, nums), cmp=lambda x, y: cmp(x + y, y + x), reverse=True)).lstrip('0') or '0'


s = Solution()
print(s.largestNumber([0]))
print(s.largestNumber([1, 2, 20]))
