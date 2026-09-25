class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        NUMS = len(arr)
        total = 0
        l, r = -1, -1
        result = 0
        while l < len(arr) - k:
            if l >= 0:
                total -= arr[l]
            l += 1
            while r < (l + k - 1):
                r += 1
                total += arr[r]
            if total / k >= threshold:
                result += 1
        return result
