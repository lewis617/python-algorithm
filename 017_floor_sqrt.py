class Solution:
    def floorSqrt(self, A):
        if(A == 0 or A == 1):
            return A
        low, high = 1, A
        mid = (low+high)/2
        while(low <= high):
            if(mid*mid == A):
                return mid
            elif(mid*mid < A):
                if((mid+1)*(mid+1) > A):
                    return mid
                else:
                    low = mid
            else:
                high = mid
            mid = (low + high)/2


s = Solution()
print(s.floorSqrt(11))
