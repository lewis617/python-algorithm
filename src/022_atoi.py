import re


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        ret = re.match(r' *([-+]?\d+)', str)
        if ret:
            ret = int(ret.group(1))
            if ret > 2**31-1:
                return 2**31-1
            if ret < -2**31:
                return -2**31
            return ret
        else:
            return 0


s = Solution()
print(s.myAtoi(' 9 wer'))
print(s.myAtoi(' wer 9'))
