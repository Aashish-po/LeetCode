class Solution:
    def findMissingElements(self, a: List[int]) -> List[int]:
        return [q for i, j in pairwise(sorted(a)) for q in range(i + 1, j)]
