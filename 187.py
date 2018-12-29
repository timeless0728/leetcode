class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        end = 10
        res = s[:10]
        reslist = set()
        dup = []
        reslist.add(res)
        while end < len(s):
            res = res[1:]+s[end]
            if res in reslist:
                if res not in dup:
                    dup.append(res)
            else:
                reslist.add(res)
            end+=1

        return dup

solu = Solution()
print solu.findRepeatedDnaSequences("AAAAAAAAAAAA")