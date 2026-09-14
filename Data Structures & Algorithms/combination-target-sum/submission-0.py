class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        length = len(nums)
        combo = []
        def dfs(idx: int, t: int):
            if t == 0:
                result.append(list(combo))
                return
            if t < 0 or idx == len(nums):
                return
            combo.append(nums[idx])
            dfs(idx, t - nums[idx])
            combo.pop()
            dfs(idx + 1, t)

        dfs(0, target)
        return result