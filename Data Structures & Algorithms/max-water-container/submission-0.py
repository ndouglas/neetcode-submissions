class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp, rp = 0, len(heights) - 1
        result = 0
        while lp < rp:
            result = max(result, (rp - lp) * min(heights[lp], heights[rp]))
            if heights[lp] == heights[rp]:
                lp += 1
                rp -= 1
            elif heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        return result