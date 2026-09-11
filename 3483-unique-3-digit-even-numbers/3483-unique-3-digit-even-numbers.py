class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        l1 = itertools.permutations(digits,3)
        l2 = []
        for i in l1:
            if i[0] != 0 and i[-1] % 2 == 0:
                l2.append(i)
        return len(set(l2))