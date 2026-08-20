class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)

        # Build bitmask for each reserved row
        for r, s in reservedSeats:
            rows[r] |= 1 << s

        ans = (n - len(rows)) * 2

        left_mask = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        middle_mask = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        right_mask = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)

        for mask in rows.values():
            left_free = (mask & left_mask) == 0
            middle_free = (mask & middle_mask) == 0
            right_free = (mask & right_mask) == 0

            if left_free and right_free:
                ans += 2
            elif left_free or middle_free or right_free:
                ans += 1

        return ans
