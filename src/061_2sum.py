class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        if len(A) <= 1:
            return []
        table = {}
        for i in range(len(A)):
            if not A[i] in table:
                if not B - A[i] in table:
                    table[B-A[i]] = [i]
                else:
                    table[B - A[i]] += [i]
            else:
                return [table[A[i]][0]+1, i+1]
        return []


s = Solution()
print(s.twoSum([2, 2, 7, 11, 15], 9))
