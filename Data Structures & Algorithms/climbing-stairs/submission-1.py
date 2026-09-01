memo = {}
memo[0] = 0
memo[1] = 1
memo[2] = 2

class Solution:
    def climbStairs(self, n: int) -> int:
        if n in memo:
            return memo[n]
        match n:
            case 0:
                return 0
            case 1:
                return 1
            case 2:
                return 2
            case _:
                memo[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
                return memo[n]