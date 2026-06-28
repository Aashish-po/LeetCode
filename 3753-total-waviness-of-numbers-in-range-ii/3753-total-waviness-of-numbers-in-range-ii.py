class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        from functools import lru_cache

        def solve(n):
            s = str(n)

            @lru_cache(None)
            def dp(i, prev_prev, prev, tight, started):
                if i == len(s):
                    return (1, 0) if started else (0, 0)

                limit = int(s[i]) if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    new_tight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(i + 1, -1, -1, new_tight, False)
                        total_count += cnt
                        total_waviness += wav
                    else:
                        if not started:
                            cnt, wav = dp(i + 1, -1, d, new_tight, True)
                            total_count += cnt
                            total_waviness += wav
                        else:
                            add = 0
                            if prev_prev != -1:
                                if prev > prev_prev and prev > d:
                                    add = 1
                                elif prev < prev_prev and prev < d:
                                    add = 1

                            cnt, wav = dp(i + 1, prev, d, new_tight, True)

                            total_count += cnt
                            total_waviness += wav + cnt * add

                return total_count, total_waviness

            return dp(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)