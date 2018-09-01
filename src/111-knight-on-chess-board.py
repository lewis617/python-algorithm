class Solution:
    def knight(self, M, N, x1, y1, x2, y2):
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        queue = [(x1, y1, 0)]
        visit = [[0 for _ in range(N)] for _ in range(M)]
        visit[x1][y1] = 1
        distanceList = [[1,2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        while queue:
            x, y, step = queue.pop(0)
            visit[x][y] = 1
            if x == x2 and y == y2:
                return step
            for d in distanceList:
                nextX = x+d[0]
                nextY = y+d[1]
                if 0<=nextX<M and 0<=nextY<N and not visit[nextX][nextY]:
                    queue.append((nextX, nextY, step + 1))
        return -1

s = Solution()
print(s.knight(8, 8, 1, 1, 8, 8))