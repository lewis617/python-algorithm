class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        A.sort()
        ans = []

        def dfs(index, target, path, deep):
            if deep == 2:
                sum2 = self.twoSum(A[index:], target)
                for i in sum2:
                    ans.append(path+i)
                return
            for i in range(index, len(A)):
                if i > index and A[i] == A[i-1]:
                    continue
                dfs(i+1, target-A[i], path+[A[i]], deep+1)
        dfs(0, B, [], 0)
        return ans

    def twoSum(self, A, B):
        map = {}
        map2 = {}
        ans = []
        for i in A:
            if i in map:
                if not i in map2:
                    ans.append([map[i], i])
                    map2[i] = 1
            else:
                map[B-i] = i
        ans.reverse()
        return ans


s = Solution()
# print(s.fourSum([1, 0, -1, 0, -2, 2], 0))

# print(s.fourSum([0, 0, 0, 0, 1, -1], 0))
print(s.fourSum([9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2 ], 0))
