class Solution(object):
    def uniquePaths(self, m, n):
        grid = [[1] * (n+1) for _ in range(m+1)]
        for i in range(2, m+1):
            for j in range(2, n+1):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                # print(grid[i][j])
        return grid[m][n]
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        