class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S = len(s)
        chars = set()
        length = 0
        l = 0
        for r in range(S):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            length = max(r - l + 1, length)
        return length