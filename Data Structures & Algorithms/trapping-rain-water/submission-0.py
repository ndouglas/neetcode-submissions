class Solution:
    def trap(self, height: List[int]) -> int:
        left_maxes = [0] * len(height)
        right_maxes = [0] * len(height)

        running_max = 0
        for i in range(len(height)):
            running_max = max(running_max, height[i])
            left_maxes[i] = running_max
        
        running_max = 0
        for i in range(len(height) - 1, -1, -1):
            running_max = max(running_max, height[i])
            right_maxes[i] = running_max

        result = 0
        for i in range(len(height)):
            result += min(left_maxes[i], right_maxes[i]) - height[i]
        return result
