class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        ans = []

        def dfs(path, invalid_sum, invalid_diff):
            # print(row, col)
            row = len(path)
            if row == A:
                queens = ['.'*i + 'Q' + '.'*(A-i-1) for i in path]
                ans.append(queens)
                return
            for col in range(A):
                if col not in path and (row + col) not in invalid_sum and (row-col) not in invalid_diff:
                    dfs(path+[col], invalid_sum +
                        [row+col], invalid_diff+[row-col])
        dfs([], [], [])

        return ans


s = Solution()
print(s.solveNQueens(4))
# print(s.solveNQueens(3))
print(s.solveNQueens(5))
