import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_points = [(x**2 + y**2, [x, y]) for x, y in points]
        return [y for x, y in sorted(new_points)[:k]]

