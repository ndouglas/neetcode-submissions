class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        NUMS = len(arr)
        lp = 0
        length = 1
        last_compare = 0
        def compare(num1: int, num2: int) -> int:
            if num1 == num2:
                return 0
            elif num1 < num2:
                return -1
            else:
                return 1
        for rp in range(1, NUMS):
            curr_compare = compare(arr[rp - 1], arr[rp])
            if curr_compare == 0:
                lp = rp
            elif curr_compare == last_compare:
                lp = rp - 1
            else:
                length = max(length, rp - lp + 1)
            last_compare = curr_compare
        return length
