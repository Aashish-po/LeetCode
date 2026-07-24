class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAXV = 2048  # values <= 1500 < 2^11, so every XOR result is < 2048
        s = sorted(set(nums))  # duplicate values can't produce new XOR combinations
        m = len(s)

        # Step 1: all pairwise XORs over distinct values (i <= j), bounded to MAXV
        pair_xor = [False] * MAXV
        for i in range(m):
            si = s[i]
            for j in range(i, m):
                pair_xor[si ^ s[j]] = True

        # Step 2: combine each reachable pair-XOR with a third element from s
        result = [False] * MAXV
        for v in range(MAXV):
            if pair_xor[v]:
                for c in s:
                    result[v ^ c] = True

        return sum(result)