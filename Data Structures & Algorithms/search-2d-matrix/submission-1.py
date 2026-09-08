import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        l, r = 0, M * N - 1
        while l <= r:
            m = math.floor(l + (r - l) / 2)
            m1 = m // N
            m2 = m % N
            val = matrix[m1][m2]
            if val > target:
                r = m - 1
            elif val < target:
                l = m + 1
            else:
                return True
        return False