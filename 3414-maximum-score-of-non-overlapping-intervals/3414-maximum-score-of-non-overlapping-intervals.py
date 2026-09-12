class Solution:  
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted(range(n), key=lambda i: intervals[i][0])
        starts, dp = [intervals[i][0] for i in arr], [
            [(0, [])] * 5 for _ in range(n + 1)
        ]
        for i in range(n - 1, -1, -1):
            row, idx = dp[i], arr[i]
            l, r, w = intervals[idx]
            nxt = bisect.bisect_right(starts, r)
            for j in range(4):
                best, sub = dp[i + 1][j + 1], dp[nxt][j]
                sc, cl = sub[0] + w, sorted(sub[1] + [idx])
                row[j + 1] = (
                    (sc, cl) if sc > best[0] or sc == best[0] and cl < best[1] else best
                )
        return dp[0][4][1]
