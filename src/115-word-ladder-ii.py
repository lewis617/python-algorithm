from collections import defaultdict
import string


class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordList, a set of string
    # @return a list of lists of string
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        graph = defaultdict(set)
        # value in seen represent depth
        seen = defaultdict(int)
        seen[beginWord] = 0
        endDepth = float('inf')
        queue = [beginWord]
        while queue:
            word = queue.pop(0)
            if seen[word] >= endDepth:
                break
            for c in string.ascii_lowercase:
                for i in range(len(word)):
                    if i != c:
                        newWord = word[:i] + c + word[i+1:]
                        # bfs maybe have seen its nephew, so if depth of newWord is 1 less than word, then it's nephew
                        if newWord in wordList and (newWord not in seen or seen[newWord] -1 == seen[word]):  
                            graph[word].add(newWord)
                            if newWord == endWord:
                                endDepth = seen[word] + 1
                            if newWord not in seen:
                                seen[newWord] = seen[word] + 1
                                queue.append(newWord)
        ans = []
        def dfs(word, path):
            if word == endWord:
                ans.append(path)
            for newWord in graph[word]:
                dfs(newWord, path + [newWord])
        dfs(beginWord, [beginWord])
        return ans
        


s = Solution()
print(s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
