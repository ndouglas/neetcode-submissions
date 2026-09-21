class Solution:
    def rob(self, nums: List[int]) -> int:
        money = [0, 0, 0]
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        d = 0
        max_got = 0
        for i in range(len(nums)):
            [a, b, c] = money
            d = nums[i] + max(a, b)
            max_got = max(d, max_got)
            money = [b, c, d]
        return max_got
