class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        total = 0
        result = 0

        for value in nums:
            total += value
            result += counts[total - k]
            counts[total] += 1
        
        return result