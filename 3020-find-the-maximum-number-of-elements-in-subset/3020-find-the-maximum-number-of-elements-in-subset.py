class Solution:
    def maximumLength(self, nums):
        freq = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in freq:
            ans = max(ans, freq[1] if freq[1] % 2 == 1 else freq[1] - 1)

        for x in freq:
            if x == 1:
                continue

            cur = x
            length = 0

            # Build STRICT power chain
            while freq[cur] >= 2 and cur * cur in freq:
                length += 1
                cur = cur * cur

            # Now decide if we can place center
            if cur in freq:
                ans = max(ans, 2 * length + 1)
            else:
                ans = max(ans, 1 if length == 0 else 2 * length - 1)

        return ans