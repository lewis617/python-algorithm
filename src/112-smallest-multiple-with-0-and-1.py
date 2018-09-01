class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        q = ['1']
        visit = set()
        while q:
            n = q.pop(0)
            rem = int(n) % A
            if rem == 0:
                return n
            if rem not in visit:
                visit.add(rem)
                q.append(n+'0')
                q.append(n+'1')