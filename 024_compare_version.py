class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        list1 = map(int, A.split('.'))
        list2 = map(int, B.split('.'))
        if len(list1) > len(list2):
            list2 += [0] * (len(list1)-len(list2))
        else:
            list1 += [0] * (len(list2)-len(list1))
        for i in range(len(list1)):
            if list1[i] > list2[i]:
                return 1
            elif list1[i] < list2[i]:
                return -1
            else:
                continue
        return 0


s = Solution()
print(s.compareVersion('1.1.2', '1.1'))
print(s.compareVersion('1.1.2', '1.10'))
print(s.compareVersion('01', '1'))
