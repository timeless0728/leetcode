class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        result = []
        has_circle = [False]
        visit_list = [0 for i in range(numCourses)]  # 0:unvisited,1:permanent,2:temp

        def visit(n):
            if visit_list[n] == 1:
                return
            if visit_list[n] == 2:
                has_circle[0] = True
                return
            visit_list[n] = 2
            for i in prerequisites:
                if i[1] == n:
                    visit(i[0])
            visit_list[n] = 1
            result.insert(0, n)

        for i in range(numCourses):
            visit(i)
        if has_circle[0]:
            return []
        else:
            return result


solu = Solution()
print solu.findOrder(2, [[0, 1], [1, 0]])
