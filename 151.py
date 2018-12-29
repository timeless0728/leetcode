class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = []
        output = []
        for i in s:
            if i == ' ':
                if word != []:
                    output.append(''.join(word))
                    word = []
                else:
                    continue
            else:
                word.append(i)
        if word:
            output.append(''.join(word))
        output.reverse()
        return ' '.join(output)
solu = Solution()
print solu.reverseWords("the  sky is blue")