class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        NUMS = len(nums)
        result = [[]]
        working = []
        def dfs(idx: int):
            if idx >= NUMS:
                return
            working.append(nums[idx])
            result.append(working.copy())
            dfs(idx + 1)
            working.pop()
            while idx < NUMS - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1)
        dfs(0)
        return result
