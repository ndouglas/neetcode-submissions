class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sums = [[0] * len(x) for x in matrix]
        for i in range(len(matrix)):
            self.prefix_sums[i][0] = matrix[i][0]
            for j in range(1, len(matrix[0])):
                self.prefix_sums[i][j] = matrix[i][j] + self.prefix_sums[i][j - 1]
            if i == 0:
                continue
            for j in range(0, len(matrix[0])):
                self.prefix_sums[i][j] += self.prefix_sums[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.prefix_sums[row2][col1 - 1] if col1 > 0 else 0
        above = self.prefix_sums[row1 - 1][col2] if row1 > 0 else 0
        overlap = self.prefix_sums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        corner = self.prefix_sums[row2][col2]
        return corner - left - above + overlap


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)