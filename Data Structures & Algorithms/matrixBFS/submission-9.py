from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        NEIGHBORS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        to_visit = deque()
        length = 0
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        visited.add((0, 0))
        to_visit.append((0, 0))

        while to_visit:
            for i in range(len(to_visit)):
                (row, col) = to_visit.popleft()
                if row == ROWS - 1 and col == COLS - 1:
                    return length
                for (dr, dc) in NEIGHBORS:
                    (nr, nc) = (row + dr, col + dc)
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    to_visit.append((nr, nc))
            length += 1
        return -1