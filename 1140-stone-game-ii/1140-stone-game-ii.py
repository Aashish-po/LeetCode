class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dfs(i: int, M: int) -> int:
            if i >= n:
                return 0

            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            opponent_best = float("inf")

            for X in range(1, 2 * M + 1):
                opponent_best = min(
                    opponent_best,
                    dfs(i + X, max(M, X))
                )

            return suffix[i] - opponent_best

        return dfs(0, 1)