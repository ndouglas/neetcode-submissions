class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * 3
        for i in range(len(nums)):
            n = nums[i]
            counts[n] += 1
        j = 0
        for i in range(len(counts)):
            while counts[i] > 0:
                nums[j] = i
                counts[i] -= 1
                j += 1
        