class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        prevRow = [0] * COLS
        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0
        for i in range(ROWS - 1, -1, -1):
            currRow = [0] * COLS
            for j in range(COLS - 1, -1, -1):
                currSum = 0
                if i == ROWS - 1 and j == COLS - 1:
                    currSum = 1
                else:
                    currSum = currRow[j + 1] if j + 1 < COLS and obstacleGrid[i][j + 1] == 0 else 0
                    currSum += prevRow[j] if i + 1 < ROWS and obstacleGrid[i + 1][j] == 0 else 0
                currRow[j] = currSum
            prevRow = currRow
        return prevRow[0]