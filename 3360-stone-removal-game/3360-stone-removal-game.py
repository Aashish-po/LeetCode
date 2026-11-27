class Solution:
    def canAliceWin(self, n: int) -> bool:
        return (10 <= n < 19) or (27 <= n < 34) or (40 <= n < 45) or (49 <= n <= 50)
