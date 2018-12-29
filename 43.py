class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if int(num1) == 0 or int(num2) == 0:
            return 0
        res_list = []
        for i in range(len(num1) - 1, -1, -1):
            res = int(num2) * int(num1[i])
            res_list.insert(0, res)
        next_num = 0
        for i in range(len(res_list)-1,-1,-1):
            if i == 0:
                res_list[i] = str(res_list[i] + next_num)
                break
            res_list[i] = res_list[i] + next_num
            if res_list[i]<10:
                res_list[i] = str(res_list[i])
                next_num = 0
                continue
            else:
                num = res_list[i]%10
                next_num = (res_list[i]-num)/10
                res_list[i] = str(num)
        return ''.join(res_list)


solu = Solution()
print solu.multiply('408','5')