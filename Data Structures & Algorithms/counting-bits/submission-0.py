class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(n + 1):
            if i == 0:
                result[i] = 0
            elif i == 1:
                result[i] = 1
            else:
                np2 = int(math.log2(i))
                result[i] = 1 + result[i - int(2**np2)]
        return result