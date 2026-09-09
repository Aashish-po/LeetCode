class Solution:
    def countCommas(self, n: int) -> int:
        ans, p1000 = 0, 1000
        while p1000 <= n:
            ans += n - (p1000 - 1)
            p1000 *= 1000
        return ans
