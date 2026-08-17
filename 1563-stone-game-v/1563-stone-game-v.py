class Solution:
    def stoneGameV(self, stones: List[int]) -> int:
        n = len(stones)
        self.stones = stones
        self.prefix_sum = self.build_prefix_sum(stones)

        dp = [[None] * n for _ in range(n)]
        best_cut = [[None] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            best_cut[i][i] = i  

        for right in range(1, n):
            left = 0
            while 0 <= left <= n - 1 and 0 <= right <= n - 1:
                max_score = -math.inf
                mid_then = None 
                for mid in range(
                    best_cut[left][right - 1] - 1, best_cut[left + 1][right] + 1 + 1
                ):
                    if not left <= mid <= right - 1:
                        continue

                    left_sum = self.value_sum(left, mid)
                    right_sum = self.value_sum(mid + 1, right)

                    if left_sum == right_sum:
                        score = max(
                            dp[left][mid] + left_sum, dp[mid + 1][right] + right_sum
                        )
                    elif left_sum < right_sum:
                        score = dp[left][mid] + left_sum
                    else:
                        score = dp[mid + 1][right] + right_sum

                    if max_score < score:
                        max_score = score
                        mid_then = mid

                dp[left][right] = max_score
                best_cut[left][right] = mid_then

                left += 1
                right += 1

        return dp[0][n - 1]

    def build_prefix_sum(self, arr):
        curr_sum = 0
        ret = []
        for num in arr:
            curr_sum += num
            ret.append(curr_sum)
        return ret

    @cache
    def value_sum(self, left, right):
        if left == 0:
            return self.prefix_sum[right]

        return self.prefix_sum[right] - self.prefix_sum[left - 1]
