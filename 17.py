def one(x,y):
    res = []
    for i in x:
        for j in y:
            res.append(j+i)
    return res

letter = lambda a,b:b if a==[] else a if b==[] else one(a,b)


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        maplist ={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        resu = []
        def getCom(i,result):
            if i==len(digits):
                return result
            else:
                return getCom(i+1,letter(maplist[digits[i]],result))

        return getCom(0,resu)

solu = Solution()
print solu.letterCombinations('23')


