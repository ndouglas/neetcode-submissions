class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = [0] * len(nums)
        self.prefix_sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.prefix_sums[i] = nums[i] + self.prefix_sums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left - 1]
