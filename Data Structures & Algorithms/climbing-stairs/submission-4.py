class Solution:
    def climbStairs(self, n: int) -> int:
        match n:
            case 0:
                return 0
            case 1:
                return 1
            case _:
                memo = [0, 1]
                for i in range(n):
                    [a, b] = memo[0], memo[1]
                    memo[0] = b
                    memo[1] = a + b
                return memo[1]