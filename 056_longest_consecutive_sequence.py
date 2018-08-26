class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        nums = set(A)
        ans = 0
        for x in nums:
            if x-1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                ans = max(ans, y-x)
        return ans


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
