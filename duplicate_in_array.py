class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        map = {}
        arr = []
        for i in A:
            if(i in map):
                arr.append(i)
            map[i] = 1
        return arr
        
s = Solution()
print(s.repeatedNumber([1,2,1]))