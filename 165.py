class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split('.')
        ver2 = version2.split('.')

        flag = 0
        max_one = ver1 if len(ver1) > len(ver2) else ver2
        length = min(len(ver1), len(ver2))
        while flag < length:
            ver1num = int(ver1[flag])
            ver2num = int(ver2[flag])
            if ver1num > ver2num:
                return 1
            elif ver2num > ver1num:
                return -1
            else:
                flag += 1
        while flag < len(max_one):
            if int(max_one[flag]) > 0:
                return 1 if len(ver1) > len(ver2) else -1
            else:
                flag += 1
        return 0


solu = Solution()
print solu.compareVersion("1.0.1", '1')
