class Solution:
    def numOfStrings(self, patterns, word):
        return sum(p in word for p in patterns)
