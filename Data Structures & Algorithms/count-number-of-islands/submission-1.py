class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        def dfs(row: int, col: int) -> bool:
            nonlocal count
            if row < 0 or col < 0 or row == ROWS or col == COLS or grid[row][col] == '0' or (row, col) in visited:
                return False

            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i, j) in visited:
                    continue
                if dfs(i, j):
                    count += 1

        return count