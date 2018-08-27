class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, combo, index):
            if remain == 0:
                result.append(combo)
                return
            for i in range(index, len(candy)):
                if i > index and candy[i] == candy[i-1]:
                    continue
                if candy[i] > remain:
                    # exceeded the sum with candidate[i]
                    break  # the for loop

                dfs(remain - candy[i], combo + [candy[i]], i+1)

        candy = sorted(candidates)
        result = []
        dfs(target, [], 0)
        return result


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([8, 10, 6, 11, 1, 16, 8], 28))
