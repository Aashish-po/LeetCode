class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # Step 1: transform
        arr = [1 if x == target else -1 for x in nums]
        
        # Step 2: prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        # Step 3: count pairs
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if prefix[j] > prefix[i]:
                    ans += 1
        
        return ans