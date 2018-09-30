class Solution():
    def countSmaller(self, nums):
        import bisect
        counts = []
        done = []
        for num in nums[::-1]:
            counts.append(bisect.bisect_left(done, num))
            bisect.insort(done, num)
        return counts[::-1]

s= Solution()
print(s.countSmaller([5,2,6,1]))