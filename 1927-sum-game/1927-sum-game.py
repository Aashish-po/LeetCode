class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        sumL = sumR = 0
        cntL = cntR = 0

        for i in range(half):
            if num[i] == '?':
                cntL += 1
            else:
                sumL += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                cntR += 1
            else:
                sumR += int(num[i])

        diff = sumL - sumR

        if (cntL + cntR) % 2:
            return True

        return diff != (cntR - cntL) * 9 // 2