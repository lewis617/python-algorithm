class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        graph = [[] for _ in range(A)]
        visit = [0 for _ in range(A)]
        for i in range(len(B)):
            p = B[i] - 1
            c = C[i] - 1
            graph[c].append(p)
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(A):
            if not dfs(i):
                return 0
        return 1

s = Solution()
print(s.solve(3, [ 1, 2, 3 ], [ 2, 3, 1 ]))