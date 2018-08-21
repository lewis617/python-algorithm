class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        seen = [[False]*cols for _ in matrix]
        arr = []
        curRow = curCol = dirIndex = 0
        dirList = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for _ in range(rows*cols):
            arr.append(matrix[curRow][curCol])
            seen[curRow][curCol] = True
            nextRow, nextCol = curRow + \
                dirList[dirIndex][0], curCol + dirList[dirIndex][1]
            if 0 <= nextRow < rows and 0 <= nextCol < cols and not seen[nextRow][nextCol]:
                curRow, curCol = nextRow, nextCol
            else:
                dirIndex = (dirIndex + 1) % 4
                curRow, curCol = curRow + \
                    dirList[dirIndex][0], curCol + dirList[dirIndex][1]
        return arr


s = Solution()
print(s.spiralOrder([[1, 2], [3, 4]]))
