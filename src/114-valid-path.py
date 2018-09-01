class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        directions = [[0, 1], [1, 1], [1, 0], [0, -1],
                      [-1, -1], [-1, 0], [1, -1], [-1, 1]]
        visit = [[0 for _ in range(B)] for _ in range(A)]
        
        for i in range(C):
                cx = E[i]
                cy = F[i]
                if abs(cx-A) <= D or abs(cy-B) <= D:
                    return 'NO'

        def dfs(x, y):
            if not 0 <= x < A or not 0 <= y < B:
                return False
            if visit[x][y]:
                return False
            for i in range(C):
                cx = E[i]
                cy = F[i]
                if abs(cx-x) <= D or abs(cy-y) <= D:
                    return False
            if x == A and y == B:
                return True
            visit[x][y] = 1
            for d in directions:
                nx = x + d[0]
                ny = y + d[1]
                dfs(nx, ny)
            return False
        return 'YES' if dfs(0, 0) else 'NO'


s = Solution()
print(s.solve(64, 81, 1, 3, [1, 27], [1, 69]))
