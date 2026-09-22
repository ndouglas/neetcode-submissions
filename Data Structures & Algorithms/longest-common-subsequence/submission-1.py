class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS = len(text1)
        COLS = len(text2)
        prevRow = [0] * (COLS + 1)
        for i in range(ROWS - 1, -1, -1):
            currRow = [0] * (COLS + 1)
            for j in range(COLS - 1, -1, -1):
                if text1[i] == text2[j]:
                    currRow[j] = 1 + prevRow[j + 1]
                else:
                    currRow[j] = max(currRow[j + 1], prevRow[j])
            prevRow = currRow
        return prevRow[0]