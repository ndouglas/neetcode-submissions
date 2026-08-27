class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_found = 0
        so_far = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                so_far += 1
                max_found = max(max_found, so_far)
            else:
                so_far = 0
        return max_found
