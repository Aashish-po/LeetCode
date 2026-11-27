class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        const int MAX_F = 1500;
        vector<int> freq(MAX_F + 1, 0);
        for (const auto& item : items) {
            freq[item[0]]++;
        }

        // multiples[f] = total count of items with factor a multiple of f
        vector<int> multiples(MAX_F + 1, 0);
        for (int f = 1; f <= MAX_F; ++f) {
            if (freq[f] > 0) {
                for (int mult = f; mult <= MAX_F; mult += f) {
                    multiples[f] += freq[mult];
                }
            }
        }

        // 0/1 Knapsack for buying at most one copy of each item (unlocking
        // freebies)
        vector<int> dp(budget + 1, -1);
        dp[0] = 0;
        int min_price = 1e9;

        for (const auto& item : items) {
            int f = item[0];
            int p = item[1];
            min_price = min(min_price, p);
            if (p > budget)
                continue;

            // Subtract 1 to exclude the item itself from its multiples
            int val = 1 + (multiples[f] - 1);
            for (int c = budget; c >= p; --c) {
                if (dp[c - p] != -1) {
                    dp[c] = max(dp[c], dp[c - p] + val);
                }
            }
        }

        // Spend remaining budget on the cheapest item (+1 item per copy)
        int ans = 0;
        for (int c = 0; c <= budget; ++c) {
            if (dp[c] != -1) {
                ans = max(ans, dp[c] + (budget - c) / min_price);
            }
        }

        return ans;
    }
};