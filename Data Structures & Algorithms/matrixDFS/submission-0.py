class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(row: int, col: int, visit: Set) -> int:
            if row < 0 or col < 0 or row == ROWS or col == COLS or (row, col) in visit or grid[row][col] == 1:
                return 0
            elif row == ROWS - 1 and col == COLS - 1:
                return 1
            
            visit.add((row, col))

            count = 0
            count += dfs(row + 1, col, visit)
            count += dfs(row - 1, col, visit)
            count += dfs(row, col + 1, visit)
            count += dfs(row, col - 1, visit)

            visit.remove((row, col))
            return count

        return dfs(0, 0, set())