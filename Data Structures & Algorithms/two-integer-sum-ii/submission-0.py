class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1
        while lp < rp:
            curr = numbers[lp] + numbers[rp]
            if curr == target:
                return [lp + 1, rp + 1]
            elif curr < target:
                lp += 1
            else:
                rp -= 1