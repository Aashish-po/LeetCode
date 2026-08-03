class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        
        # Prefix sum for O(1) range queries
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]
        
        # Memoization: dp[i] = max advantage (score difference) from position i
        memo = {}
        
        def max_advantage(pos: int) -> int:
            if pos >= n:
                return 0  # No stones left
            
            if pos in memo:
                return memo[pos]
            
            best = float('-inf')
            
            # Try taking 1, 2, or 3 stones
            for take in range(1, 4):
                if pos + take > n:
                    break
                
                stones_score = prefix_sum[pos + take] - prefix_sum[pos]
                advantage = stones_score - max_advantage(pos + take)
                best = max(best, advantage)
            
            memo[pos] = best
            return best
        
        alice_advantage = max_advantage(0)
        
        if alice_advantage > 0:
            return "Alice"
        elif alice_advantage < 0:
            return "Bob"
        else:
            return "Tie"