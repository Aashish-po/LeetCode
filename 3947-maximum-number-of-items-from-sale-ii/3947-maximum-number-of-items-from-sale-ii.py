class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        global_min_p = float("inf")

        for f, p in items:
            freq[f] += 1
            if p < global_min_p:
                global_min_p = p

        # mult_count[f] = total number of items whose factor is a multiple of f
        mult_count = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] > 0:
                total = 0
                for m in range(f, n + 1, f):
                    total += freq[m]
                mult_count[f] = total

        # Build (price, max_2_item_copies) for each individual item
        bundles = []
        for f, p in items:
            c_i = mult_count[f] - 1
            if c_i > 0:
                bundles.append((p, c_i))

        bundles.sort()

        total_items = 0
        rem = budget

        for p, count in bundles:
            if p > 2 * global_min_p:
                break
            can_buy = min(count, rem // p)
            total_items += can_buy * 2
            rem -= can_buy * p
            if can_buy < count:
                break

        total_items += rem // global_min_p
        return total_items
