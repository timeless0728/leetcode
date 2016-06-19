# http://www.novaroma.org/via_romana/numbers.html


calc = lambda numb, size: (numb - numb % size) / size


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        unit = [1000, 500, 100, 50, 10, 5, 1]
        string = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        cal_str = ''
        for i in range(len(unit)):
            if calc(num, unit[i]) == 4 and len(cal_str) > 0 and cal_str[-1] == string[i - 1]:
                cal_str = cal_str[:-1] + string[i] + string[i - 2]
            elif calc(num, unit[i]) == 4:
                cal_str = cal_str + string[i] + string[i - 1]
            else:
                for j in range(calc(num, unit[i])):
                    cal_str += string[i]
            num = num - unit[i] * calc(num, unit[i])
        return cal_str


solution = Solution()
