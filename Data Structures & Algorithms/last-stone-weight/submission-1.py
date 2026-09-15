import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) >= 2:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x != y:
                heapq.heappush_max(stones, max(x, y) - min(x, y))
        return 0 if not len(stones) else stones[0]