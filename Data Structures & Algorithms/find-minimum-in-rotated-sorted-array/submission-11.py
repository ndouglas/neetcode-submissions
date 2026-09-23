class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp < rp:
            mp = lp + (rp - lp) // 2
            ln = nums[lp]
            rn = nums[rp]
            mn = nums[mp]
            if mn <= nums[(mp - 1) % len(nums)] and mn <= nums[(mp + 1) % len(nums)]:
                return mn
            elif mn > rn:
                lp = mp + 1
            else:
                rp = mp - 1
        return nums[lp]