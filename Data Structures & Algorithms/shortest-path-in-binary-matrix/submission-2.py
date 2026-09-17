from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        NEIGHBORS = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        queue = deque()
        visited = set()
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        queue.append((0, 0))
        visited.add((0, 0))
        length = 1

        while queue:
            for i in range(len(queue)):
                (row, col) = queue.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                for (dr, dc) in NEIGHBORS:
                    (nr, nc) = (row + dr, col + dc)
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            length += 1

        return -1