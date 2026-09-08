import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def getHoursForRate(k: int) -> int:
            res = 0
            for i in range(len(piles)):
                val = piles[i]
                res += math.ceil(val / k)
            return res

        def isAcceptable(k: int) -> bool:
            return getHoursForRate(k) <= h

        l, r = 1, max(piles)
        sol = 1000000000
        while l <= r:
            m = math.floor(l + (r - l) / 2)
            if isAcceptable(m):
                sol = min(m, sol)
                r = m - 1
            else:
                l = m + 1
        return sol