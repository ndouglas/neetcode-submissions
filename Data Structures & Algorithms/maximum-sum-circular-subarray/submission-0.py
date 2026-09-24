class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        glob_max, glob_min = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total = 0

        for num in nums:
            curr_max = max(curr_max + num, num)
            glob_max = max(glob_max, curr_max)
            curr_min = min(curr_min + num, num)
            glob_min = min(glob_min, curr_min)
            total += num
        
        if glob_max > 0:
            return max(glob_max, total - glob_min)
        return glob_max