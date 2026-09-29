import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1
        def is_alphanumeric(text):
            pattern = r"^[a-zA-Z0-9]$"
            return bool(re.match(pattern, text))
        while lp <= rp:
            while lp <= rp and not is_alphanumeric(s[lp]):
                lp += 1
            while lp <= rp and not is_alphanumeric(s[rp]):
                rp -= 1
            if lp <= rp and not s[lp].upper() == s[rp].upper():
                return False
            lp += 1
            rp -= 1
        return True