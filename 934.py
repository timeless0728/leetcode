class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        group1 = []
        select = [[0 for i in A[0]] for j in A]
        found = False
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 1:
                    if len(group1) == 0:
                        self.findgroup(group1, i, j, A, select)
                        found = True
                    break
            if found:
                break

        pick = group1

        count = 0
        while pick:
            new_pick = set()
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            print pick,count
            for [i, j] in pick:
                for [m, n] in directions:
                    if len(A) > i + m >= 0 and len(A) > j + n >= 0:
                        if A[i + m][j + n] == 1:
                            return count
                        elif A[i + m][j + n] == 0:
                            A[i + m][j + n] = 2
                            new_pick.add((i + m, j + n))
            pick = new_pick
            count += 1

    def findgroup(self, group, i, j, A, select):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        if select[i][j] == 0:
            select[i][j] = 1

            inner = True
            for [m, n] in directions:
                if len(A) > i + m >= 0 and len(A) > j + n >= 0 and A[i + m][j + n] == 0:
                    inner = False

            A[i][j] = 2 if not inner else 3
            if not inner:
                group.append([i, j])

            for [m, n] in directions:
                if len(A) > i + m >= 0 and len(A) > j + n >= 0 and A[i + m][j + n] == 1:
                    self.findgroup(group, i + m, j + n, A, select)


solu = Solution()
print solu.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]])
