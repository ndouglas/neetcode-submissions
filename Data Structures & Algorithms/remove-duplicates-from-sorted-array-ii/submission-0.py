class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        read, write = 2, 2
        while read < len(nums):
            if nums[write - 2] != nums[read]:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write