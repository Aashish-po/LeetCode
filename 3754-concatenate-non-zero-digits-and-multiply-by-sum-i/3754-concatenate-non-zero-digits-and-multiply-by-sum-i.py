class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0

        for ch in str(n):
            d = int(ch)
            if d != 0:
                x = x * 10 + d
                digit_sum += d

        return x * digit_sum