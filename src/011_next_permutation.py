class Solution:
    def nextPermutation(self, nums):
        l = len(nums)
        partition = -1
        for i in range(l-1, -1, -1):
            if nums[i-1] < nums[i]:
                partition = i-1
                break
        if partition == -1:
            nums.reverse()
            return nums
        else:
            for i in range(l-1, partition, -1):
                if(nums[i]>nums[partition]):
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
        nums[partition+1:len(nums)]=nums[partition+1:len(nums)][::-1]
        return nums


s = Solution()
print(s.nextPermutation([1, 2, 3]))
print(s.nextPermutation([5, 4, 3, 2, 1]))
print(s.nextPermutation([5, 4, 6, 8, 7]))
