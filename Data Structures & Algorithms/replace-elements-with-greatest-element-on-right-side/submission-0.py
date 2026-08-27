class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = -1
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                curr = arr[i]
                arr[i] = -1
            elif curr >= arr[i]:
                arr[i] = curr
            else:
                pos = i
                tmp = arr[i]
                arr[i] = curr
                curr = tmp
    
        return arr