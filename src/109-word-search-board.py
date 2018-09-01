class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        if not A:
            return 0
        A = [list(s) for s in A]

        def dfs(word, x, y):
            if not word:
                return 1
            if x < 0 or x >= len(A) or y < 0 or y >= len(A[0]) or word[0] != A[x][y]:
                return 0
            temp = A[x][y]
            A[x][y] = '#'
            ans = dfs(word[1:], x+1, y) or dfs(word[1:], x-1,
                                               y) or dfs(word[1:], x, y+1) or dfs(word[1:], x, y-1)
            A[x][y] = temp
            return ans
        for i in range(len(A)):
            for j in range(len(A[0])):
                if dfs(B, i, j):
                    return 1
        return 0


s = Solution()
grid = ["FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA",
        "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF"]
print(s.exist(grid, 'BCDCB'))
