class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_non_zero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True
                
        # If total XOR is non-zero, take all elements
        if total_xor != 0:
            return len(nums)
        
        # If total XOR is 0, but there's a non-zero element, remove 1 element
        if has_non_zero:
            return len(nums) - 1
            
        # All elements are 0
        return 0