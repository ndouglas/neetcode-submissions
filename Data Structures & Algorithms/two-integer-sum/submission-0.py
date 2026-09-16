class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in map:
                return [map[remainder], i]
            if nums[i] not in map:
                map[nums[i]] = i
        