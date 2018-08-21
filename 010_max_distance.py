class Solution:
    def maximumGap(self, array):
        arr = []
        for idx, i in enumerate(array):
            arr.append((i, idx))
        arr.sort()
        print(arr)
        current = arr[0][1]
        diff = -1
        for i in arr:
            if i[1] < current:
                current = i[1]
            else:
                diff = max(i[1] - current, diff)
        return diff


s = Solution()

print(s.maximumGap([3, 6, 2, 7]))
print(s.maximumGap([1, 1, 1, 1]))
print(s.maximumGap([1]))
