class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit_list = [0 for i in range(numCourses)]  # 0:unvisited,1:permanent,2:temp
        if prerequisites == []:
            return True

        def visit(n):
            if visit_list[n] == 1:
                return True
            if visit_list[n] == 2:
                return False
            visit_list[n] = 2
            res = all(visit(i[0]) for i in prerequisites if i[1] == n)
            visit_list[n] = 1
            return res
        return all([visit(i[0]) for i in prerequisites])


solu = Solution()
print solu.canFinish(3, [[2, 1], [1, 0]])
