class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word: return False
        rows, cols = len(board), len(board[0])
        ds = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(path):
            if len(path) == len(word):
                return True
            curR, curC = path[-1]
            for d in ds:
                nextR, nextC = curR+d[0], curC+d[1]
                if 0 <= nextR < rows and 0 <= nextC < cols and (nextR, nextC) not in path and board[nextR][nextC] == word[len(path)]:
                    if dfs(path+[(nextR, nextC)]):
                        return True
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs([(r,c)]):
                        return True
        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
"ABCEFSADEESE"))
