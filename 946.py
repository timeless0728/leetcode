class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        pop = 0
        push = 0
        stack = []
        while pop < len(popped) and push < len(pushed):
            stack.append(pushed[push])
            print stack, 'append'
            push += 1
            while stack and popped[pop] == stack[-1]:
                stack.pop()
                print stack, 'pop'
                pop += 1
        print stack
        if stack:
            return False
        return True


solu = Solution()
print solu.validateStackSequences([1, 0, 2], [2, 1, 0])
