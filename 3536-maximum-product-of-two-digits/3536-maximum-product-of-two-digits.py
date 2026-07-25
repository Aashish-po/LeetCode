class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(c) for c in str(n)]
        best = 0
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                best = max(best, digits[i] * digits[j])
        return best