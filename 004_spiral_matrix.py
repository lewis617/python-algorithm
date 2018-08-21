class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 右下左上
        currentR = currentC = di = 0
        for _ in range(R * C):
            ans.append(matrix[currentR][currentC])
            seen[currentR][currentC] = True
            nextR, nextC = currentR + directions[di][0], currentC + directions[di][1]
            if 0 <= nextR < R and 0 <= nextC < C and not seen[nextR][nextC]:
                currentR, currentC = nextR, nextC
            else:
                di = (di + 1) % 4
                currentR, currentC = currentR + directions[di][0], currentC + directions[di][1]
        return ans


s = Solution()
print(s.spiralOrder([[1, 2], [3, 4]]))
