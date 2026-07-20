class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total  

        result = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                flat = r * n + c
                new_flat = (flat + k) % total  
                nr, nc = divmod(new_flat, n)
                result[nr][nc] = grid[r][c]
        return result