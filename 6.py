class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        r = []
        new_index = 0
        if numRows ==1:
            return s
        for i in range(numRows):
            key = i
            times = 1
            while new_index < len(s) and key < len(s):
                print i, key,new_index,times
                r.append(s[key])
                new_index += 1
                if i == 0 or i == numRows - 1:
                    key += 2 * (numRows - 1)
                elif times % 2 == 0:
                    key += 2 * i
                else:
                    key += 2 * (numRows - i - 1)

                times += 1
        return ''.join(r)


solu = Solution()
print solu.convert('ab', 1)
