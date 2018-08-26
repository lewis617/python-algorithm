import sys


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        l = len(A)
        ans = A[0] + A[1] + A[-1]
        for i in range(l-2):
            j = i + 1
            k = l - 1
            while j < k:
                new_sum = A[i] + A[j] + A[k]
                diff = abs(ans - B)
                new_diff = abs(new_sum - B)

                if diff > new_diff:
                    ans = new_sum
                if new_sum < B:
                    j += 1
                elif new_sum > B:
                    k -= 1
                else:
                    return new_sum

        return ans


s = Solution()
# print(s.threeSumClosest([1, 2, 3, 4], 10))
print(s.threeSumClosest([-5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6,
                         0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3], -1))
