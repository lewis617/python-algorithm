class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r in [0, rows-1] or c in [0, cols - 1]):
                    queue.append((r, c))
        while queue:
            r, c = queue.pop(0)
            board[r][c] = 'D'
            for d in dirs:
                r1, c1 = r + d[0], c + d[1]
                if 0 <= r1 < rows and 0 <= c1 < cols and board[r1][c1] == 'O':
                    queue.append((r1, c1))
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'D':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
        return board


s = Solution()
print(s.solve([["X", "X", "X", "X"],
               ["X", "O", "O", "X"],
               ["X", "X", "O", "X"],
               ["X", "O", "X", "X"]]))
