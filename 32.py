def getStack(s,stack):
    for i in s:
        if i == '(':
            stack+=(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack=stack[:-1]
                stack+='2'
            else:
                stack+=i
        else:
            stack=stack[:-1]+str(i)+stack[-1]
    if s==stack:
        return stack
    print stack
    return getStack(stack,'')


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        maxcount = 0

        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop(-1)
                    count +=2
                    if maxcount<count:
                        maxcount=count
                else:
                    stack=[]
                    count = 0
            print stack

        return maxcount

solu = Solution()
print solu.longestValidParentheses("()(()")