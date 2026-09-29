class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer, reader = 1, 1
        while reader < len(nums):
            if nums[reader] != nums[writer - 1]:
                nums[writer] = nums[reader]
                writer += 1
            reader += 1
        return writer