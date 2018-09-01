class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        if sum(A) < sum(B):
            return -1
        start, total, Min = 0, 0, 0
        for i in range(len(A)):
            total += A[i] - B[i]
            if total < Min:
                start = (i + 1) % len(A)
                Min = total
        return start


s = Solution()
print(s.canCompleteCircuit([1, 2], [2, 1]))
print(s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(s.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
print(s.canCompleteCircuit(
    [383, 521, 491, 907, 871, 705], [96, 197, 592, 67, 77, 641]))
