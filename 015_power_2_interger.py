import math


class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, n):
        # Base case
        if (n <= 1):
            return 1
        if(n == 2):
            return 0

        # Try all numbers from 2 to sqrt(n)
        # as base
        for x in range(2, (int)(math.sqrt(n)) + 1):
            p = x

            # Keep multiplying p with x while
            # is smaller than or equal to x
            while (p <= n):
                p = p * x

                if (p == n):
                    return 1
        return 0


s = Solution()
print(s.isPower(9))
print(s.isPower(4))
