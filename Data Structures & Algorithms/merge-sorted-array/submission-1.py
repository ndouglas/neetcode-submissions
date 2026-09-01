class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1p = m - 1
        n2p = n - 1
        wp = m + n - 1
        while wp >= 0:
            n1 = nums1[n1p] if n1p >= 0 else -10000000000
            n2 = nums2[n2p] if n2p >= 0 else -10000000000
            if n1 >= n2:
                nums1[wp] = n1
                wp -= 1
                n1p -= 1
            else:
                nums1[wp] = n2
                wp -= 1
                n2p -= 1
