class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1
        while lp < rp:
            mp = lp + (rp - lp) // 2
            ln = nums[lp]
            rn = nums[rp]
            mn = nums[mp]
            sdir = target - mn # naively; +=R, -=L
            if mn == target:
                return mp
            elif ln > mn: # reset to left
                if rn >= target and target > mn:
                    lp = mp + 1
                else:
                    rp = mp - 1
            else: # reset to right
                if ln <= target and target < mn:
                    rp = mp - 1
                else:
                    lp = mp + 1
        if nums[lp] == target:
            return lp
        else:
            return -1
