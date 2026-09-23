class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [(temperatures[-1], len(temperatures) - 1)]
        for i in range(len(temperatures) - 2, -1, -1):
            dt = temperatures[i]
            while stack and stack[-1][0] <= dt:
                stack.pop()
            if stack and stack[-1][0] > dt:
                result[i] = stack[-1][1] - i
            else:
                result[i] = 0
            stack.append((dt, i))
        return result
