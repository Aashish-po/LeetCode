class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            # only values achievable: all triplets from {1..n}, degenerate small case
            vals = set()
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        vals.add(nums[i] ^ nums[j] ^ nums[k])
            return len(vals)
        bits = n.bit_length()
        return 1 << bits