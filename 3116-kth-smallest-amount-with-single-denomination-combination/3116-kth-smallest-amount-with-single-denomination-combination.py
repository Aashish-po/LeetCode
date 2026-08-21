class Solution:
    def findKthSmallest(self, coins, k):
        n = len(coins)
        m = 1 << n
        lcm = [1] * m
        bits = [0] * m

        for mask in range(1, m):
            for i in range(n):
                if mask & (1 << i):
                    lcm[mask] = lcm[mask] // gcd(lcm[mask], coins[i]) * coins[i]
                    bits[mask] += 1

        def count(x):
            ans = 0
            for mask in range(1, m):
                if lcm[mask] <= x:
                    v = x // lcm[mask]
                    ans += v if bits[mask] % 2 else -v
            return ans

        lo, hi = k, min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo