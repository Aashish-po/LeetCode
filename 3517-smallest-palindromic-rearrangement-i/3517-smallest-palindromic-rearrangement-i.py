class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        # Count frequencies
        freq = Counter(s)
        
        # Build left half greedily with smallest chars first
        left_half = []
        middle = ""
        
        for char in sorted(freq):
            count = freq[char]
            left_half.extend([char] * (count // 2))
            if count % 2:
                middle = char
        
        left_str = "".join(left_half)
        return left_str + middle + left_str[::-1]
