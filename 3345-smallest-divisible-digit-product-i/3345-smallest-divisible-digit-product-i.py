class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x):
            prod = 1
            while x:
                prod *= x % 10
                x //= 10
            return prod

        num = n
        while True:
            if digit_product(num) % t == 0:
                return num
            num += 1
