class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        max_int = pow(2, 31) - 1
        min_int = pow(2, 31)
        positive = True
        res = 0
        if dividend < 0:
            positive = not positive
            dividend = -dividend
        if divisor < 0:
            positive = not positive
            divisor = -divisor
        if dividend == 0 or divisor == 1:
            compare = max_int if positive else min_int
            res = dividend if dividend < compare else compare
        else:
            def cur(dividend, res):
                if dividend < divisor:
                    return res
                new_divisor = divisor
                times = 1
                while dividend >= new_divisor:
                    dividend -= new_divisor
                    res += times
                    new_divisor += new_divisor
                    times += times
                return cur(dividend, res)
            res = cur(dividend, res)

        return res if positive else -res


print pow(2, 31) - 1
solu = Solution()
print solu.divide(2147483647, 2)
