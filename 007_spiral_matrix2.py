class Solution(object):
    def spiralOrder(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        rows = cols = n
        curRow = curCol = dirIndex = 0
        dirList = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(rows*cols):
            matrix[curRow][curCol] = i + 1
            nextRow, nextCol = curRow + \
                dirList[dirIndex][0], curCol + dirList[dirIndex][1]
            if 0 <= nextRow < rows and 0 <= nextCol < cols and matrix[nextRow][nextCol] == 0:
                curRow, curCol = nextRow, nextCol
            else:
                dirIndex = (dirIndex + 1) % 4
                curRow, curCol = curRow + \
                    dirList[dirIndex][0], curCol + dirList[dirIndex][1]
        return matrix


s = Solution()
print(s.spiralOrder(3))
print(s.spiralOrder(0))
