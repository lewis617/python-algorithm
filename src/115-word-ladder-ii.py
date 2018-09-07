from collections import defaultdict
import string


class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordList, a set of string
    # @return a list of lists of string
    def findLadders(self, beginWord, endWord, wordList):
        level = {beginWord}
        parents = defaultdict(set)
        while level and endWord not in parents:
            next_level = defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = node[:i]+char+node[i+1:]
                        if n in wordList and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res


s = Solution()
print(s.findLadders('hit', 'cog', {"hot", "dot", "dog", "lot"}))
