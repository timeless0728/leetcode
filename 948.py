class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens = sorted(tokens)
        point = 0
        max_point = 0
        start = 0
        end = len(tokens) - 1
        if len(tokens) == 1:
            return 1 if tokens[0] < P else 0
        while start < end and point >= 0:
            while P >= tokens[start]:
                point += 1
                P -= tokens[start]
                start += 1
            while P < tokens[start]:
                max_point = max(max_point, point)
                point -= 1
                P += tokens[end]
                end -= 1

        return max_point


solu = Solution()
print solu.bagOfTokensScore([71, 55, 82], 54)
