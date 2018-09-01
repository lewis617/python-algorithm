class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        A = [list(s) for s in A]

        def dfs(x, y):
            if not 0 <= x < len(A) or not 0 <= y < len(A[0]) or A[x][y] != 'X':
                return
            A[x][y] = 'Y'
            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x-1, y)
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 'X':
                    dfs(i, j)
                    ans += 1
        return ans


s = Solution()
print(s.black([
    'OOOXOOO',
    'OOXXOXO',
    'OXOOOXO']))
