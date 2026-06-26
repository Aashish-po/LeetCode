class Solution:
    def countMajoritySubarrays(self, nums, target):
        return self.countSubarrays(nums, target)
    
    def countSubarrays(self, nums, target):
        from bisect import bisect_left, insort

        arr = [1 if x == target else -1 for x in nums]

        prefix = 0
        ans = 0
        sorted_prefix = [0]

        for v in arr:
            prefix += v
            ans += bisect_left(sorted_prefix, prefix)
            insort(sorted_prefix, prefix)

        return ans
