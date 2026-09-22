import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freqs = [[] for i in range(len(nums) + 1)]
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        for num, cnt in counts.items():
            freqs[cnt].append(num)
        
        result = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                result.append(num)
                if len(result) == k:
                    return result