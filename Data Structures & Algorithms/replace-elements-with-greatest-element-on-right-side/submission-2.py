class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max_val = -1
        # reverse iteration
        # new max_val = max(max_val, arr[i])
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(max_val, arr[i])
            arr[i] = max_val
            max_val = new_max
        return arr