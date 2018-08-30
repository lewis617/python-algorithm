class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        if A == A[::-1]:
            return 0
        for i in range(len(A)):
            if A[:i] == A[:i][::-1] and A[i:] == A[i:][::-1]:
                return 1
        cut = [i for i in range(-1, len(A))]
        for i in range(len(A)):
            r1 = r2 = 0
            while i-r1>=0 and i+r1<len(A) and A[i-r1] == A[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            while i-r2>=0 and i+1+r2 < len(A) and A[i-r2] == A[i+1+r2]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2+=1
        return cut[-1]
                
