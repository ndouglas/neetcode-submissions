class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        bits = 32
        for i in range(bits):
            result |= 1 << (bits - i - 1) if (n & 1 << i) > 0 else 0
        return result