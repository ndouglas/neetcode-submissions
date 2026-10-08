class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        NUMS = len(nums)
        result = [[]]
        working = []
        def dfs(idx: int):
            if idx == NUMS:
                return
            working.append(nums[idx])
            result.append(working.copy())
            dfs(idx + 1)
            working.pop()
            dfs(idx + 1)
        dfs(0)
        return result