class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        NUMS = len(nums)
        visited = [False] * NUMS
        permutations = []

        def dfs():
            if len(permutations) == NUMS:
                result.append(permutations.copy())
                return

            for i in range(NUMS):
                if visited[i]:
                    continue

                if i and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                permutations.append(nums[i])
                dfs()
                visited[i] = False
                permutations.pop()

        nums.sort()
        dfs()

        return result        