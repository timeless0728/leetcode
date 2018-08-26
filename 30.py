def isSub(string,substrList):
    for i in range(len(substrList)):
        if string[i*len(substrList[0]):(i+1)*len(substrList[0])]


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
