class Solution(object):
    def minDistance(self, word1, word2):
        length1 = len(word1)
        length2 = len(word2)
        grid = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(length1 + 1):
            for j in range(length2 + 1):
                if i==0 or j==0:
                    if i == 0:
                        grid[i][j] = j
                    else:
                        grid[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    grid[i][j] = grid[i - 1][j - 1]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1], grid[i-1][j-1]) + 1
        return grid[length1][length2]

        
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        