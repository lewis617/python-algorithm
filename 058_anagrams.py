class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        hashmap = {}
        for i in range(len(A)):
            st = A[i]
            key = ''.join(sorted(st))
            if key not in hashmap:
                hashmap[key] = [i+1]
            else:
                hashmap[key] += [i+1]
        ans = hashmap.values()
        ans.reverse()
        return ans


s = Solution()
print(s.anagrams(['cat', 'dog', 'god', 'tac']))
