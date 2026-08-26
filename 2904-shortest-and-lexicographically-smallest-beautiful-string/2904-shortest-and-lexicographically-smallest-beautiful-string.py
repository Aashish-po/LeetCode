class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""

        for i in range(len(s)):
            ones = 0

            for j in range(i, len(s)):
                if s[j] == '1':
                    ones += 1

                if ones > k:
                    break

                if ones == k:
                    cur = s[i:j + 1]

                    if not ans:
                        ans = cur
                    elif len(cur) < len(ans):
                        ans = cur
                    elif len(cur) == len(ans) and cur < ans:
                        ans = cur

        return ans