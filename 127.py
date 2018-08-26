import Queue


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        q = Queue.Queue()
        a = {}
        if beginWord in wordList:
            wordList.remove(beginWord)
        q.put(beginWord)
        a[beginWord] = 1
        visit = set()
        while not q.empty():
            tmp = q.get()
            if tmp == endWord:
                return a[endWord]
            if tmp not in visit:
                visit.add(tmp)
                for i in range(len(tmp)):
                    pd1, pd2 = tmp[:i], tmp[i + 1:]
                    for j in wordList:
                        pd3, pd4 = j[:i], j[i + 1:]
                        print tmp,j
                        if j != tmp and pd1 == pd3 and pd2 == pd4:
                            q.put(j)
                            a[j] = a[tmp] + 1
                            visit.add(j)
                            print q.queue, a, visit,tmp

        return 0


solu = Solution()
print solu.ladderLength('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])
print solu.ladderLength('a', 'c', ['a','b','c'])
