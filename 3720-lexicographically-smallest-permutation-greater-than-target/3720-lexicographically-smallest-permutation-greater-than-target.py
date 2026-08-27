class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1

        pivot = -1

        for i in range(n):
            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if freq[c]:
                    pivot = i
                    break

            if freq[x] == 0:
                break

            freq[x] -= 1

        if pivot == -1:
            return ""

        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1

        for i in range(pivot):
            freq[ord(target[i]) - 97] -= 1

        x = ord(target[pivot]) - 97

        for c in range(x + 1, 26):
            if freq[c]:
                freq[c] -= 1
                break

        result = target[:pivot] + chr(c + 97)

        for i in range(26):
            if freq[i]:
                result += chr(i + 97) * freq[i]

        return result