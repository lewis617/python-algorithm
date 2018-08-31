class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        last_max_reach, current_max_reach = 0 , 0
        njump , i = 0 , 0
        while current_max_reach < len(A)-1:
            while i <= last_max_reach:
                current_max_reach = max(i+A[i],current_max_reach)
                i+=1
            if last_max_reach == current_max_reach:
                return -1
            last_max_reach = current_max_reach
            njump+=1
        return njump
