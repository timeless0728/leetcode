class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = []
        start=0
        end = 0
        max_len = 0

        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
            else:
                start+=1
            max_len = max(max_len, end-start)
        return max_len


solu = Solution()
print solu.lengthOfLongestSubstring("pwwkew")
