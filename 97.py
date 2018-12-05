# -*- coding:utf-8 -*-

# s3中只会有s1和s2，写一个二维数组就可以了

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        res_list = [[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0 and j==0:
                    res_list[i][j] = True
                elif i==0:
                    res_list[i][j] = res_list[i][j-1] & (s2[j-1] == s3[j-1])
                elif j == 0:
                    res_list[i][j] = res_list[i-1][j] & (s1[i-1] == s3[i-1])
                else:
                    res_list[i][j] = (res_list[i][j-1]&(s2[j-1]==s3[i+j-1])) or  (res_list[i-1][j]&(s1[i-1]==s3[i+j-1]))

        return res_list[len(s1)][len(s2)]


solu = Solution()
print solu.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
