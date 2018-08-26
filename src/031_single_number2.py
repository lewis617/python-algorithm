class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        count = [0] * 32
        for i in A:
            for j in range(32):
                count[j] += (i >> j) & 1
                # number that show 3 times are clear, then count[j] will be (i)th bit of number that show once
                count[j] %= 3
        # turn bit list (I mean count) to number
        ans = 0
        for i in range(32):
            ans += (count[i] << i)
        return ans


s = Solution()
print(s.singleNumber([1, 1, 1, 2]))
