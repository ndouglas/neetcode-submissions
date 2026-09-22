class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        bits = 32
        for i in range(bits):
            bit = (n >> i) & 1
            result += (bit << (31 - i))
        return result