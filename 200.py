class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.findisland(i, j, grid)
                    count += 1
        return count

    def findisland(self, i, j, grid):
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        grid[i][j] = 2
        for item_x, item_y in directions:
            if 0 <= i + item_x < len(grid) and 0 <= j + item_y < len(grid[0]) and grid[i + item_x][j + item_y] == '1':
                self.findisland(i + item_x, j + item_y, grid)
        return grid

solu = Solution()
print solu.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])