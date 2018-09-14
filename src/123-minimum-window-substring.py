import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_map, count = collections.Counter(t), len(t),
        start = end = head = 0
        d = float('inf')
        while end < len(s):
            if t_map[s[end]] > 0:
                count -= 1
            t_map[s[end]] -= 1
            end += 1
            while count == 0:
                if (end - start) < d:
                    d = end - start
                    head = start
                t_map[s[start]] += 1
                if t_map[s[start]] >0:
                    count += 1
                start += 1
        return "" if d == float('inf') else s[head:head + d]

s=Solution()
print(s.minWindow('ADOBECODEBANC', ''))