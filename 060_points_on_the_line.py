class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        ans = 0
        for i in range(len(A)):
            hashmap = {'vertical': 1}
            same = 0
            for j in range(i+1, len(A)):
                if B[i] == B[j]:
                    if A[i] == A[j]:
                        same += 1
                        continue
                    else:
                        slope = 'vertical'
                else:
                    slope = (A[i] - A[j])*1.0/(B[i] - B[j])
                if slope in hashmap:
                    hashmap[slope] += 1
                else:
                    hashmap[slope] = 2
            ans = max(max(hashmap.values())+same, ans)

        return ans


s = Solution()
print(s.maxPoints([1, 2, 3, 4, 5, 5], [1, 2, 3, 4, 5, 5]))
print(s.maxPoints([-1], [-1]))
