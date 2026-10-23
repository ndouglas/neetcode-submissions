class Solution:
    def helper(self, i: int, nums: List[int]) -> List[List[int]]:
        if i == len(nums):
            return [[]]
        result = []
        permutations = self.helper(i + 1, nums)
        for p in permutations:
            for j in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(j, nums[i])
                result.append(pCopy)
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums)