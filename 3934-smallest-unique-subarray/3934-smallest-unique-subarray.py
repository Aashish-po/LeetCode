class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        def check(arr, size, base):
            m = len(arr)
            mp = defaultdict(int)
            MOD = 10**9 + 7
            power = (base ** (size - 1)) % MOD
            hash_value = 0

            for i in range(m):
                hash_value = (hash_value * base + nums[i]) % MOD

                if i >= size - 1:
                    mp[hash_value] += 1
                    hash_value = (hash_value - (nums[i - size + 1] * power)) % MOD

            for key, count in mp.items():
                if count == 1:
                    return True
            return False

        n = len(nums)
        low, high = 1, n
        base = max(nums) + 1
        res = 0

        while low <= high:
            mid = (low + high) // 2

            if check(nums, mid, base):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
