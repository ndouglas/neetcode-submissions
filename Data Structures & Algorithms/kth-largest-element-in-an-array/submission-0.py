import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            num = nums[i]
            heapq.heappush_max(heap, num)
        for i in range(k - 1):
            heapq.heappop_max(heap)
        return heapq.heappop_max(heap)