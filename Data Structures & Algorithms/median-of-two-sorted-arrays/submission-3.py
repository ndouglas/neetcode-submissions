class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2        
        if len(A) > len(B):
            A, B = B, A
        if len(A) == 0:
            A = B
        total = len(A) + len(B)
        half = total // 2
        l, r = 0, len(A)
        while True:
            i = l + (r - l) // 2  # A
            j = half - i - 2      # B
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j + 1 < len(B) else float("infinity")
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
                return min(Aright, Bright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1