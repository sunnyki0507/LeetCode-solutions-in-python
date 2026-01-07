class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        row = len(text1)
        column = len(text2)
        grid = [[0] * (column+1) for _ in range(row+1)]
        for i in range(row-1, -1,-1):
            for j in range(column-1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i+1][j+1]
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        return grid[0][0]
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        