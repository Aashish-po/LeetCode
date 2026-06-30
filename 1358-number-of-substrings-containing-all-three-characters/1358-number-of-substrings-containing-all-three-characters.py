class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_a = last_b = last_c = -1
        result = 0

        for i, ch in enumerate(s):
            if ch == 'a':
                last_a = i
            elif ch == 'b':
                last_b = i
            else:
                last_c = i
            
            if last_a != -1 and last_b != -1 and last_c != -1:
                result += min(last_a, last_b, last_c) + 1

        return result