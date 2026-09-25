class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        NUMS = len(nums)
        window = set()
        l, r = -1, -1
        while l < NUMS:
            if l >= 0:
                window.remove(nums[l])
            l += 1
            while r < min(NUMS - 1, l + k):
                r += 1
                if nums[r] in window:
                    return True
                window.add(nums[r])
        return False