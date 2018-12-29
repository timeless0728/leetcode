class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        import math
        res = []
        for i in tokens:
            if i == '+' or i == '-' or i == '*' or i == '/':
                res1 = float(res.pop())
                res2 = float(res.pop())
                if i == '/':
                    resnum = res2/res1
                    if resnum>0:
                        new_res = math.floor(resnum)
                    else:
                        new_res = math.ceil(resnum)
                elif i == '+':
                    new_res = res2+res1
                elif i == '-':
                    new_res = res2-res1
                elif i == '*':
                    new_res = res2*res1
                res.append(new_res)
            else:
                res.append(i)
        return int(res[0])


solu = Solution()
print solu.evalRPN(

["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
