class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        TEMPS = len(temperatures)
        result = [0] * TEMPS
        for i in range(TEMPS - 2, -1, -1):
            j = i + 1
            while j < TEMPS and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    j = TEMPS
                    break
                j += result[j]                
            if j < TEMPS:
                result[i] = j - i
        return result
