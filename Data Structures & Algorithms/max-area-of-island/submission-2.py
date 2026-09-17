class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0

        def dfs(row: int, col: int) -> int:
            if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == 0:
                return 0

            area = 1            
            grid[row][col] = 0
            
            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)

            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:                    
                    max_area = max(max_area, dfs(i, j))

        return max_area