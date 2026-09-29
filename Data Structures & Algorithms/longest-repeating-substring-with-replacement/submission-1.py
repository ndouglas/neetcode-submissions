class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxf = 0
        result = 0
        lp = 0
        for rp in range(len(s)):
            count[s[rp]] += 1
            maxf = max(count[s[rp]], maxf)
            while (rp - lp + 1) - maxf > k:
                count[s[lp]] -= 1
                lp += 1
            result = max(result, rp - lp + 1)
        return result
