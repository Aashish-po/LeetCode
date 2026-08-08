class Solution:
    def validSequence(self, a: str, b: str) -> list[int]:
        n = len(a)
        m = len(b)

        # c[i] = how many characters of b are still unmatched
        # after greedily matching suffix using a[i:]
        c = [0] * (n + 1)

        d = m - 1
        for i in range(n - 1, -1, -1):
            if d >= 0 and a[i] == b[d]:
                d -= 1
            c[i] = d + 1

        e = [0] * m
        f = 0  # current position in b
        g = 0  # whether mismatch has been used
        
        for i in range(n):
            if f>=m:
                break
                
            if a[i] == b[f]:
                e[f] = i
                f += 1

            elif g == 0 and c[i + 1] <= f + 1:
                e[f] = i
                f += 1
                g = 1

        if f < m:
            return []

        return e