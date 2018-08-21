class Solution:
    def generate(self, n):
        if n == 0:
            return []
        elif n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1, 1]]
        elif n > 2:
            ans = [[] for i in range(n)]
            for i in range(n):
                ans[i] = [1 for i in range(i+1)]
            for i in range(2, n):
                for j in range(1, i):
                    ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
            return ans

s = Solution()
print(s.generate(5))
print(s.generate(0))