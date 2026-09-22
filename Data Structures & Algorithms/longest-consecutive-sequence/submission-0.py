class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_found = 0
        curr_found = 0
        for i in range(len(nums)):
            num = nums[i]
            curr_found = 1
            if num - 1 in my_set:
                continue
            while num + 1 in my_set:
                curr_found += 1
                num += 1
            max_found = max(curr_found, max_found)
        return max_found
