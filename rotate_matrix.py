def rotate(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return A
        rows = len(A)
        cols = len(A[0])
        
        for r in range(0, rows):
            for c in range(r, cols):
                A[r][c], A[c][r] = A[c][r], A[r][c]
        for row in A:
            row = row.reverse()
        return A
