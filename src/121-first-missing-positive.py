class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        # use the index as the hash to record the frequency of each number
        for i in range(len(nums)):
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i]/n == 0:
                return i
        return n


s = Solution()
print(s.firstMissingPositive([1,2,0]))
