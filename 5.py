class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==1:
            return s
        r = ['']
        for j in range(len(s)):
            r.append(s[j])
            r.append('')
        left = 0
        right = 0
        step = 1
        for i in range(len(r)):
            while (i - step) >= 0 and (i + step) < len(r):
                if r[i - step:i + step + 1] == r[i + step:i - step-1:-1]:
                    left = i - step
                    right = i + step
                    step += 1
                else:
                    break
        return ''.join(r[left:right + 1])


solu = Solution()
print solu.longestPalindrome('ccc')
