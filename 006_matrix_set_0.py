class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        zeroRows = [False] * rows
        zeroCols = [False] * cols
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroRows[r] = True
                    zeroCols[c] = True
        for r in range(len(zeroRows)):
            for c in range(len(zeroCols)):
                if zeroRows[r] or zeroCols[c]:
                    matrix[r][c] = 0
        return matrix


s = Solution()

print(s.setZeroes([[1, 0, 2], [1, 3, 4], [4, 5, 6]]))
