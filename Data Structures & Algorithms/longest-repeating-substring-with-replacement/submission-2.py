class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        result = 0
        lp = 0
        max_freq = 0

        for rp in range(len(s)):
            count[s[rp]] += 1
            max_freq = max(max_freq, count[s[rp]])
            while (rp - lp + 1) - max_freq > k:
                count[s[lp]] -= 1
                lp += 1
            result = max(result, rp - lp + 1)

        return result
