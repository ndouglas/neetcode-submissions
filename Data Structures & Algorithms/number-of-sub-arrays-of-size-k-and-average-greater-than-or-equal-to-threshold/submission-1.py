class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        NUMS = len(arr)
        THRESHOLD = threshold * k
        result = curr_sum = 0
        for r in range(len(arr)):
            curr_sum += arr[r]
            if r >= k - 1:
                result += curr_sum >= THRESHOLD
                curr_sum -= arr[r - k + 1]
        return result
