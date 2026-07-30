class Solution:
    def minimumPushes(self, word: str) -> int:
        total_pushes = 0

        for i in range(len(word)):
            cost = (i // 8) + 1
            total_pushes += cost

        return total_pushes
