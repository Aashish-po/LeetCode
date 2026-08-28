class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = -1
        for i in range(26):
            if cnt[i] & 1:
                if odd != -1:
                    return ""
                odd = i

        half = [c // 2 for c in cnt]
        m = n // 2

        def build(left_half: str) -> str:
            if odd != -1:
                return (
                    left_half
                    + chr(ord('a') + odd)
                    + left_half[::-1]
                )
            return left_half + left_half[::-1]

        target_left = target[:m]

        remaining = half[:]
        possible = True

        for ch in target_left:
            idx = ord(ch) - ord('a')
            if remaining[idx] == 0:
                possible = False
                break
            remaining[idx] -= 1

        if possible:
            candidate = build(target_left)
            if candidate > target:
                return candidate

        for i in range(m - 1, -1, -1):
            remaining = half[:]

            valid_prefix = True
            for j in range(i):
                idx = ord(target_left[j]) - ord('a')
                if remaining[idx] == 0:
                    valid_prefix = False
                    break
                remaining[idx] -= 1

            if not valid_prefix:
                continue

            cur = ord(target_left[i]) - ord('a')

            for nxt in range(cur + 1, 26):
                if remaining[nxt] == 0:
                    continue

                rem = remaining[:]
                rem[nxt] -= 1

                left = list(target_left[:i])
                left.append(chr(ord('a') + nxt))

                for c in range(26):
                    left.extend(chr(ord('a') + c) for _ in range(rem[c]))

                left_half = "".join(left)
                return build(left_half)

        return ""