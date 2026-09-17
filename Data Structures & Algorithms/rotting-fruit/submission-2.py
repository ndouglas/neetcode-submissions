from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        NEIGHBORS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rotten = set()
        fresh = set()
        queue = deque()
        time = 0

        def markOranges():
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 2:
                        rotten.add((i, j))
                        queue.append((i, j))
                    elif grid[i][j] == 1:
                        fresh.add((i, j))
        
        markOranges()

        while queue:
            if not fresh:
                return time
            for i in range(len(queue)):
                (row, col) = queue.popleft()
                for (dr, dc) in NEIGHBORS:
                    (nr, nc) = (row + dr, col + dc)
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr, nc) not in fresh or (nr, nc) in rotten:
                        continue
                    rotten.add((nr, nc))
                    fresh.remove((nr, nc))
                    queue.append((nr, nc))
            time += 1
        
        return -1 if fresh else time