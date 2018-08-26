class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0:
            return 'MAX_INT'
        if dividend==0:
            return 0
        else:
            i = 0
            newone = 0
            if divisor>0>dividend:
                while newone >= dividend:
                    newone -= divisor
                    i -= 1
                return i+1
            elif dividend>0>divisor:
                while newone <= dividend:
                    newone -= divisor
                    i -= 1
                return i+1
            elif dividend>0:
                while newone <= dividend:
                    newone += divisor
                    i += 1
                return i-1
            else:
                while newone >= dividend:
                    newone += divisor
                    i += 1
                return i-1

solu =Solution()
print solu.divide(1,2)