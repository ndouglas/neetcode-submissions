class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = defaultdict(int)
        map_t = defaultdict(int)
        for i in range(len(s)):
            map_s[s[i]] += 1
            map_t[t[i]] += 1
        for i in range(len(s)):
            if map_s[s[i]] != map_t[s[i]]:
                return False
            if map_s[t[i]] != map_t[t[i]]:
                return False
        return True