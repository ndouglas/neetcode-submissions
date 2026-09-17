class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0]) 
        START = image[sr][sc]

        def dfs(row: int, col: int):
            if row < 0 or col < 0 or row == ROWS or col == COLS or image[row][col] != START or image[row][col] == color:
                return
            
            image[row][col] = color

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

            return

        dfs(sr, sc)

        return image