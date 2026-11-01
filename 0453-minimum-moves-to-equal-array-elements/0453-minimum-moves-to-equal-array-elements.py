class Solution:
    def minMoves(self, a: list[int]) -> int:
        return sum(a) - min(a) * len(a)
