class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        res = [l, r, 0]
        while l < r:
            contain = 0 if height[r] == 0 or height[l] == 0 else (r - l) * min(height[r], height[l])
            if contain > res[2]:
                res = [l, r, contain]
            if height[r] - height[l] < 0:
                r = r - 1
            elif height[r] - height[l] > 0:
                l = l + 1
            else:
                l = l + 1
        return res[2]


solution = Solution()
