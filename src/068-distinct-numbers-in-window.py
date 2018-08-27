class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        ans = []
        hashmap = {}
        count = 0
        for i in range(B):
            if not A[i] in hashmap:
                hashmap[A[i]] = 1
                count += 1
            else:
                hashmap[A[i]] += 1
        ans.append(count)
        for i in range(B, len(A)):
            if hashmap[A[i - B]] == 1:
                count -= 1
                del hashmap[A[i - B]]
            else:
                hashmap[A[i - B]] -= 1
            if not A[i] in hashmap:
                hashmap[A[i]] = 1
                count += 1
            else:
                hashmap[A[i]] += 1
            ans.append(count)
        return ans


s = Solution()
print(s.dNums([1, 2, 1, 3, 4, 3], 3))
