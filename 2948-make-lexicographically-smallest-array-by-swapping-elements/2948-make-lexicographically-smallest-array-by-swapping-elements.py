class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        arr = sorted((num, i) for i, num in enumerate(nums))
        ans = [0] * n

        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            values = []
            indices = []

            for k in range(start, end + 1):
                values.append(arr[k][0])
                indices.append(arr[k][1])

            indices.sort()

            for idx, val in zip(indices, values):
                ans[idx] = val

            start = end + 1

        return ans
